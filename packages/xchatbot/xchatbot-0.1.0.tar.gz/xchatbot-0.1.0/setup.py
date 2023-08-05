#!/usr/bin/env python
import sys
import os
from setuptools import setup

with open('README.md', 'r') as f:
    readme = f.read()

# 'setup.py publish' shortcut.
if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist bdist_wheel')
    os.system('twine upload dist/*')
    sys.exit()

setup(name='xchatbot',
    version='0.1.0',
    description='the Xtensible XMPP Chat Bot',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Fabiio Comuni',
    author_email='fabrixxm@gmail.com',
    url='https://git.sr.ht/~fabrixxm/xchatbot',
    py_modules=['xchatbot'],
    data_files=['./echobot.rc.dist'],
    install_requires=[
        'nbxmpp>=0.6.10,<0.7.0',
        'PyGObject>=3.30.0,<3.40.0',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3',
        'Topic :: Communications :: Chat',
    ]
)