#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import os

from pathlib import Path

from python_hosts import Hosts, HostsEntry

from procrust import __description__


storage = Path('~/.procrust').expanduser()
block_file = Path(storage, 'block.txt')


def init():
    storage.mkdir()
    block_file.touch()
    Hosts().write(path=Path(storage, 'hosts.original'))


def edit():
    if not storage.exists():
        init()

    # Windows only
    if getattr(os, 'startfile', None):
        os.startfile(block_file)
    # Other OS
    else:
        editor = os.environ.get('EDITOR')
        if editor:
            os.system(f'{editor} {block_file}')


def start():
    hosts = Hosts()
    for host in block_file.read_text().splitlines():
        hosts.remove_all_matching(name=host)
    hosts.write()


def stop():
    hosts = Hosts()
    for host in block_file.read_text().splitlines():
        entry = HostsEntry(entry_type='ipv4', address='127.0.0.1', names=[host])
        hosts.add([entry])
    hosts.write()


def main():
    parser = argparse.ArgumentParser(description=__description__)
    subparsers = parser.add_subparsers()
    subparsers.add_parser('edit', description='Edit the list of blocked sites.').set_defaults(func=edit)
    subparsers.add_parser('start', description='Start procrastinating.').set_defaults(func=start)
    subparsers.add_parser('stop', description='Stop procrastinating.').set_defaults(func=stop)
    args = parser.parse_args()
    if getattr(args, 'func', None):
        args.func()


if __name__ == '__main__':
    main()