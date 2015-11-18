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

    # FIMXE Find a more elegent way to check if unicode
    @classmethod
    def _get_repr(cls, arg):
        if isinstance(arg, str) or repr(arg)[0:2] == 'u"':
            return arg
        return repr(arg)

    @classmethod
    def ok(cls, arg):
        """
            Prints in blue to stdout
        """
        print(cprint.colors['OK'] + cls._get_repr(arg) + cprint.colors['ENDC'],
              file=sys.stdout)

    @classmethod
    def info(cls, arg):
        """
            Prints in green to stdout
        """
        print(cprint.colors['INFO'] + cls._get_repr(arg) + cprint.colors['ENDC'],
              file=sys.stdout)

    @classmethod
    def warn(cls, arg):
        """
            Prints in yellow to strerr
        """
        print(cprint.colors['WARNING'] + cls._get_repr(arg) + cprint.colors['ENDC'],
              file=sys.stderr)

    @classmethod
    def err(cls, arg, interrupt=False):
        """
            Prints in brown to stderr
            interrupt=True: stops the program
        """
        print(cprint.colors['ERR'] + cls._get_repr(arg) + cprint.colors['ENDC'],
              file=sys.stderr)
        if interrupt:
            print(cprint.colors['ERR'] + "Error: Program stopped." +
                  cprint.colors['ENDC'],
                  file=sys.stderr)
            exit(1)

    @classmethod
    def fatal(cls, arg, interrupt=False):
        """
            Prints in red to stderr
            interrupt=True: stops the program
        """
        print(cprint.colors['FATAL'] + cls._get_repr(arg) + cprint.colors['ENDC'],
              file=sys.stderr)
        if interrupt:
            print(cprint.colors['FATAL'] + "Fatal error: Program stopped." +
                  cprint.colors['ENDC'],
                  file=sys.stderr)
            exit(1)