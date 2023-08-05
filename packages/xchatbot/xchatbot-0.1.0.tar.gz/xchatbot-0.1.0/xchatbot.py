#!/usr/bin/env python
"""
xchatbot - the Xtensible xmpp Chat Bot

Build an XMPP bot extending the base class `XChatBot`
"""

import sys
import os
import logging
from datetime import datetime
import collections
import pickle
import shlex
from functools import wraps

import nbxmpp
try:
    from gi.repository import GLib
except ImportError:
    import glib as GLib





#BOT logger
logger = logging.getLogger(__name__) # pylint: disable=invalid-name
logger.setLevel('DEBUG')
logger.addHandler(logging.StreamHandler())



# utility because the simplexml is.. too simple
# pylint: disable=invalid-name
def getTagAll(tag, tagname, **attrs):
    """
    search for a tag named `tagname` which is child of `tag`
    optionally with matching attributes
    """
    checkattrs = len(attrs.keys()) > 0
    for child in tag.getChildren():
        if child.getName() == tagname:
            if not checkattrs or all([child.getAttr(k) == v for k, v in attrs.items()]):
                return child
        granchild = getTagAll(child, tagname, **attrs)
        if granchild is not None:
            return granchild
    return None

def store(name, data):
    """store `data` as pickle value to `name.data` file"""
    with open(name + ".data", "wb") as fp:
        pickle.dump(data, fp)

def load(name, default):
    """
    Load pickled data from `name.data` file.
    If file does not exists, returns `default`
    """
    if not os.path.isfile(name + ".data"):
        return default
    with open(name + ".data", "rb") as fp:
        return pickle.load(fp)


def private(func):
    """
    Decorator to mark command private for admin user

    ```
    class MyBot(XChatBot):
        @private
        def cmd_admin(self, peer, *args):
            ...
    ```
    """
    @wraps(func)
    def command_wrapper(self, peer, *args):
        if peer.jid != self.admin_jid:
            return
        func(self, peer, *args)
    command_wrapper.is_private = True
    return command_wrapper


class Peer:
    """
    The peer that sent the message

    properites:
        jid: the peer jid
        nick: the nickname
        is_admin: true if the peer is a bot admin
        is_groupchat: true if the peer wrote to the bot is in a MUC
    """
    def __init__(self, bot, jid, nick, is_groupchat=False):
        self.bot = bot
        self.jid = jid
        self.nick = nick
        self.is_admin = jid == self.bot.admin_jid
        self.is_groupchat = is_groupchat

    def send(self, message):
        """
        Send `message` to the peer
        """
        if self.is_groupchat:
            self.bot.send_groupchat_to(self.jid, message)
        else:
            self.bot.send_message_to(self.jid, message)

    def __str__(self):
        return "{} <{} > {}".format(
            self.nick, self.jid,
            " in a groupchat" if self.is_groupchat else ""
        )


# main class
class XChatBot:
    """
        The Xtensible xmpp Chat Bot

        Subclass XChatBot and define command methods as, e.g.

        `def cmd_echo(self, peer, *args)`

        to define an "echo" command.

        example:

        ```
        from xchatbot import XChatBot


        class EchoBot(XChatBot):
            def cmd_echo(self, peer, *args):
                peer.send(" ".join(args))

        EchoBot.start()
        ```
    """
    def __init__(self, jidparams):
        self.jid = nbxmpp.protocol.JID(jidparams['jid'])
        self.password = jidparams['password']
        self.muc_nick = jidparams.get("muc_nick", "xbot")
        self.sm = nbxmpp.Smacks(self) # Stream Management
        self.client_cert = None
        self.client = None

        self.admin_jid = nbxmpp.protocol.JID(jidparams['admin']).getStripped()

        self.accept_presence = jidparams.get("accept_presence_request", False)
        self.accept_muc_invite = jidparams.get("muc_accept_invite", False)

        self.conferences = set()
        mucs = jidparams.get("mucs", "").strip()
        if mucs != "":
            self.conferences.update(mucs.split(";"))
        self.conferences.update(load("mucs", []))
        self.conferences_lastmessage = collections.defaultdict(str)
        print("conferences", self.conferences)

        self.seen_ids = load("ids", collections.deque(maxlen=1000))

        self.timer_ms = 15000

        self.ignore_before = datetime.now()

        self.commands = {}
        for name in dir(self):
            func = getattr(self, name)
            if name.startswith("cmd_") and callable(func):
                cmd = name.replace("cmd_", "")
                self.commands[cmd] = func

    @classmethod
    def start(cls):
        """
        Start bot
        """
        conf = loadconf(cls.__name__.lower())

        # GO GO GO!
        bot = cls(conf)
        bot.connect()
        try:
            ml = GLib.MainLoop()
            ml.run()
        except KeyboardInterrupt:
            bot.disconnect()
        except Exception:
            print("Unable to run the glib main loop")


    ## manage xmpp connection
    def connect(self):
        """
            Connect to the server
        """
        logger.debug("connecting to %s", self.jid.getDomain())
        idle_queue = nbxmpp.idlequeue.get_idlequeue()
        self.client = nbxmpp.NonBlockingClient(
            domain=self.jid.getDomain(),
            idlequeue=idle_queue,
            caller=self
        )
        self.client.connect(
            on_connect=self._on_connected,
            on_connect_failure=self._on_connection_failed,
            on_stream_error_cb=self._on_stream_error,
            secure_tuple=('tls', '', '', None, None)
        )

    def send_message(self, message):
        """
            Send `nbxmpp.protocol.Message`
        """
        id_ = self.client.send(message)
        self._add_seeenid(id_)
        logger.debug('sent message with id %s', id_)

    def send_message_to(self, to_jid, text):
        """
            Send a chat message to `to_jid`
        """
        id_ = self.client.send(nbxmpp.protocol.Message(to_jid, text, typ='chat'))
        self._add_seeenid(id_)
        logger.debug('sent message to %s with id %s', to_jid, id_)

    def send_groupchat_to(self, to_jid, text):
        """
            Send a groupchat message to `to_jid`
        """
        id_ = self.client.send(nbxmpp.protocol.Message(to_jid, text, typ='groupchat'))
        self._add_seeenid(id_)
        logger.debug('sent groupchat message to %s with id %s', to_jid, id_)

    def send_received(self, to_jid, message_id):
        """
            Send a message delivery receipt for `message_id` to `to_jid`
        """
        message = nbxmpp.protocol.Message(to_jid)
        message.setTag('received', namespace=nbxmpp.protocol.NS_RECEIPTS, attrs={'id': message_id})
        self.client.send(message)
        logger.debug('sent message delivery receipt for id %s', message_id)

    def quit(self):
        """Quit the bot"""
        self.disconnect()
        #ml.quit()

    def disconnect(self):
        """Disconnect from the server"""
        self.client.disconnect(message="Hop!")

    def _on_auth(self, con, auth):
        if not auth:
            logger.error('could not authenticate!')
            sys.exit()
        logger.debug('authenticated using %r', auth)

        self.client.Dispatcher.RegisterHandler("message", self._on_message)
        GLib.timeout_add(self.timer_ms, self.on_timer)

        self.client.Dispatcher.RegisterHandler(
            "presence", self._on_presence_request, typ="subscribe")

        self.client.sendPresence()
        self.client.send(nbxmpp.protocol.Presence(
            show=True, status="Ricordati! Che devi morire!"))

        for muc_jid in self.conferences:
            self.enter_muc(muc_jid)
        logger.debug("Ready to go.")

    def _on_connected(self, con, con_type):
        logger.debug('connected with %r', con_type)
        self.client.auth(
            self.jid.getNode(), self.password,
            resource=self.jid.getResource(), sasl=1, on_auth=self._on_auth)

    def get_password(self, cb, mech):
        cb(self.password)

    def _on_connection_failed(self):
        logger.error('could not connect!')

    def _on_stream_error(self, *args, **kwargs):
        logger.error("!on_stream_error %r %r", args, kwargs)

    ## / manage xmpp connection

    ## manage xmpp events

    def _event_dispatcher(self, realm, event, data):
        # print("%r, %r, %r" % (realm, event, data))
        pass

    def _on_presence_request(self, dispatcher, message):
        logger.debug("presence request %r", message)
        from_jid = message.getAttr("from")
        if from_jid != self.jid.getStripped():
            # https://xmpp.org/rfcs/rfc3921.html#rfc.section.2.2.1
            if self.accept_presence or from_jid == self.admin_jid:
                self.send_message(
                    nbxmpp.protocol.Presence(to=from_jid, typ="subscribed"))
            else:
                self.send_message(
                    nbxmpp.protocol.Presence(to=from_jid, typ="unsubscribed"))

    def _on_message(self, dispatcher, message):
        logger.debug("on_message %s", message)

        if message.getAttr("type") == "error":
            logger.error("error: %r", message)
            return

        if message.getTag("received") is not None:
            message = getTagAll(message, "message")

        if message is None:
            return

        message_id = message.getAttr("id")
        if message_id in self.seen_ids:
            return

        delay = getTagAll(message, "delay") or getTagAll(message, "x", xmlns="jabber:x:delay")
        if delay is not None:
            stamp = delay.getAttr("stamp")
            fmt = "%Y-%m-%dT%H:%M:%SZ"
            if "-" not in stamp:
                fmt = "%Y%m%dT%H:%M:%S"
            stampdatetime = datetime.strptime(stamp, fmt)
            if stampdatetime < self.ignore_before:
                return

        self._add_seeenid(message_id)

        myself = [self.jid.getStripped()] + [muc + "/" + self.muc_nick for muc in self.conferences]
        frm = str(message.getAttr("from"))
        if any([frm.startswith(me) or me.startswith(frm) for me in myself]):
            logger.debug("drop message event from self")
            return

        # TODO: skip history messages

        # manage invite to MUC
        if self.accept_muc_invite and getTagAll(message, "invite") is not None:
            conference = getTagAll(message, "x", xmlns=nbxmpp.protocol.NS_CONFERENCE)
            logger.debug("invited to %r", conference.getAttr("jid"))
            self.enter_muc(conference.getAttr("jid"))
            return

        if message.getAttr("type") == "chat":
            self._parse_message(message)

        if message.getAttr("type") == "groupchat":
            self._parse_message(message, True)


    def enter_muc(self, muc_jid):
        """Join a multiuser conference"""
        muc_jid_nick = muc_jid + "/" + self.muc_nick
        logger.debug("send presence to %s", muc_jid_nick)
        x = nbxmpp.simplexml.Node("x", attrs={"xmlns":"http://jabber.org/protocol/muc"})
        presence = nbxmpp.protocol.Presence(to=muc_jid_nick, payload=[x], attrs={"from": self.jid})
        logger.debug(presence)
        self.send_message(presence)
        self._add_conference(muc_jid)


    def _add_conference(self, muc_jid):
        if muc_jid not in self.conferences:
            self.conferences.add(muc_jid)
            store("mucs", self.conferences)


    def _add_seeenid(self, id_):
        self.seen_ids.append(id_)
        store("ids", self.seen_ids)

    ## / manage xmpp events

    ## bot logic

    def _parse_message(self, message, groupchat=False):
        bodytag = getTagAll(message, "body")
        if bodytag is None:
            logger.debug("can't find body tag!")
            return

        body = bodytag.getData().strip()
        logger.debug("parse_message: %r", body)

        from_jid_full = message.getAttr("from")
        from_jid = nbxmpp.protocol.JID(from_jid_full).getStripped()

        nick = ""
        if groupchat:
            nick = nbxmpp.protocol.JID(from_jid_full).getResource()
        else:
            nick = from_jid.split("@", 1)[0]

        if getTagAll(message, "request", xmlns=nbxmpp.protocol.NS_RECEIPTS):
            self.send_received(from_jid, message.getAttr("id"))

        peer = Peer(self, from_jid, nick, groupchat)

        logger.debug("from %s", peer)

        ### check groupchat command
        if groupchat:
            tag = "!"+self.muc_nick
            if body.startswith(tag):
                body = body.replace(tag, "").strip()
            else:
                logger.debug("last message in %s : %s", from_jid, body)
                self.conferences_lastmessage[from_jid] = body
                return


        ## parse commands

        body = body.strip()

        ### help
        if body.lower() in ["help", "aiuto", "guida", "?"]:
            self.do_help(peer)
            return


        cmdline = shlex.split(body)
        if len(cmdline) > 0:
            cmd = cmdline[0]
            args = cmdline[1:]
            if cmd in self.commands:
                self.commands[cmd](peer, *args)

    def do_help(self, peer):
        """send help message"""
        logger.debug("do_help")
        msg = "This bot reply to:\n"
        msg += "help - this message\n"
        for name, func in self.commands.items():
            if not getattr(func, "is_private", False) or peer.jid == self.admin_jid:
                msg += "{} - {}\n".format(name, func.__doc__)
        peer.send(msg)

    # Bot callbacks

    def on_timer(self):
        """timer callback"""





## ENTRY POINT

def loadconf(botname='xchatbot'):
    """
    load and parse config file 'botname.rc'
    looks in $PWD/botname.rc, ~/.botname.rc and /etc/botname.rc

    botname is the bot class name, lowercase
    """
    jidparams = {}
    confiles = [
        '{}.rc'.format(botname),
        '{}/.{}.rc'.format(os.environ['HOME'], botname),
        '/etc/{}.rc'.format(botname)
    ]
    confile = None
    for cf in confiles:
        if os.access(cf, os.R_OK):
            confile = cf
            break
    if confile is None:
        print("Can't find config file in " + ", ".join(confiles))
        sys.exit(1)

    for ln in open(confile).readlines():
        ln = ln.strip()
        if ln != "" and not ln[0] in ('#', ';'):
            key, val = ln.strip().split('=', 1)
            if val.lower() == "false":
                val = False
            elif val.lower() == "true":
                val = True
            jidparams[key.lower()] = val

    for mandatory in ['jid', 'password', 'admin']:
        if mandatory not in jidparams.keys():
            print('Please point {} config file to valid JID.'.format(confile))
            sys.exit(2)

    if "logger" in jidparams:
        logger.setLevel(jidparams['logger'])

    return jidparams




if __name__ == "__main__":
    class EchoBot(XChatBot):
        """Demo echo bot"""
        def cmd_echo(self, peer, *args):
            """echo back the text"""
            peer.send(" ".join(args))

        @private
        def cmd_admin(self, peer, *args):
            """admin command"""
            peer.send("Greetings, Professor Falken.")

    EchoBot.start()
