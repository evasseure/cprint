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
        'ENDC': '\033[0m',
        'BOLD': '\033[1m'
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
    def _check_is_bold(cls, bold):
        return cprint.colors["BOLD"] if bold else ""

    @classmethod
    def ok(cls, arg, *args, bold=False, **kwargs):
        """
            Prints in blue to stdout
            bold=True: Prints in bold.
        """
        print(cprint.colors['OK'] + cls._check_is_bold(bold) + cls._get_repr(arg) + cprint.colors['ENDC'],
              file=sys.stdout, *args, **kwargs)

    @classmethod
    def info(cls, arg, *args, bold=False, **kwargs):
        """
            Prints in green to stdout
            bold=True: Prints in bold.
        """
        print(cprint.colors['INFO'] + cls._check_is_bold(bold) + cls._get_repr(arg) + cprint.colors['ENDC'],
              file=sys.stdout, *args, **kwargs)

    @classmethod
    def warn(cls, arg, *args, bold=False, **kwargs):
        """
            Prints in yellow to stderr
            bold=True: Prints in bold.
        """
        print(cprint.colors['WARNING'] + cls._check_is_bold(bold) + cls._get_repr(arg) + cprint.colors['ENDC'],
              file=sys.stderr, *args, **kwargs)

    @classmethod
    def err(cls, arg, interrupt=False, fatal_message="Fatal error: Program stopped.", *args, bold=False, **kwargs):
        """
            Prints in brown to stderr
            interrupt=True: stops the program
            bold=True: Prints in bold. Fatal message will not be bold.
        """
        print(cprint.colors['ERR'] + cls._check_is_bold(bold) + cls._get_repr(arg) + cprint.colors['ENDC'],
              file=sys.stderr, *args, **kwargs)
        if interrupt:
            print(cprint.colors['ERR'] + fatal_message +
                  cprint.colors['ENDC'],
                  file=sys.stderr)
            exit(1)

    @classmethod
    def fatal(cls, arg, interrupt=False, fatal_message="Fatal error: Program stopped.", *args, bold=False, **kwargs):
        """
            Prints in red to stderr
            interrupt=True: stops the program
            bold=True: Makes text bold. Fatal message will not be printed in bold.
        """
        print(cprint.colors['FATAL'] + cls._check_is_bold(bold) + cls._get_repr(arg) + cprint.colors['ENDC'],
              file=sys.stderr, *args, **kwargs)
        if interrupt:
            print(cprint.colors['FATAL'] + fatal_message +
                  cprint.colors['ENDC'],
                  file=sys.stderr)
            exit(1)
