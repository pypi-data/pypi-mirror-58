#!/usr/bin/env python
__version__ = '0.1.0'

from .auth import run as auth_run
from sys import argv
from .actions import dm, post, read, chat

def define_action(api):
    if argv[1] == 'read':
        read(argv, api)
    elif argv[1] == 'post':
        post(argv, api)
    elif argv[1] == 'dm':
        dm(argv, api)
    elif argv[1] == 'chat':
        chat(argv, api)
    else:
        print("Wrong!")

def run():
    api = auth_run()
    define_action(api)

if __name__ == '__main__':
    run()