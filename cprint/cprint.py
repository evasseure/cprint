# coding: utf8
#!/usr/bin/env python
"""
    Usage:
        >>> from cprint import *
        >>> cprint.info(str)
        >>> ...
"""

from __future__ import print_function, unicode_literals
import sys


class cprint(object):

    colors = {
        'NONE': '\033[0m',
        'OK': '\033[94m',
        'INFO': '\033[92m',
        'WARNING': '\033[93m',
        'ERR': '\033[91m',
        'FATAL': '\033[31m',
        'ENDC': '\033[0m'
    }

    def __init__(self, str):
        """
            Prints in white to stdout
        """
        print(str, file=sys.stdout)
        del self

    @classmethod
    def _get_repr(cls, arg):
        if isinstance(arg, str):
            return arg
        return repr(arg)

    @classmethod
    def ok(cls, arg, *args, **kwargs):
        """
            Prints in blue to stdout
        """
        print(cprint.colors['OK'] + cls._get_repr(arg) + cprint.colors['ENDC'],
              file=sys.stdout, *args, **kwargs)

    @classmethod
    def info(cls, arg, *args, **kwargs):
        """
            Prints in green to stdout
        """
        print(cprint.colors['INFO'] + cls._get_repr(arg) + cprint.colors['ENDC'],
              file=sys.stdout, *args, **kwargs)

    @classmethod
    def warn(cls, arg, *args, **kwargs):
        """
            Prints in yellow to strerr
        """
        print(cprint.colors['WARNING'] + cls._get_repr(arg) + cprint.colors['ENDC'],
              file=sys.stderr, *args, **kwargs)

    @classmethod
    def err(cls, arg, interrupt=False, fatal_message="Fatal error: Program stopped.", *args, **kwargs):
        """
            Prints in brown to stderr
            interrupt=True: stops the program
        """
        print(cprint.colors['ERR'] + cls._get_repr(arg) + cprint.colors['ENDC'],
              file=sys.stderr, *args, **kwargs)
        if interrupt:
            print(cprint.colors['ERR'] + fatal_message +
                  cprint.colors['ENDC'],
                  file=sys.stderr)
            exit(1)

    @classmethod
    def fatal(cls, arg, interrupt=False, fatal_message="Fatal error: Program stopped.", *args, **kwargs):
        """
            Prints in red to stderr
            interrupt=True: stops the program
        """
        print(cprint.colors['FATAL'] + cls._get_repr(arg) + cprint.colors['ENDC'],
              file=sys.stderr, *args, **kwargs)
        if interrupt:
            print(cprint.colors['FATAL'] + fatal_message +
                  cprint.colors['ENDC'],
                  file=sys.stderr)
            exit(1)
