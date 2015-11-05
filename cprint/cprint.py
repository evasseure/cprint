# coding: utf8
#!/usr/bin/env python
"""
    Usage:
        >>> from cprint import *
        >>> cprint.info(str)
        >>> ...
"""

from __future__ import print_function
import sys


class cprint(object):

    colors = {
        'NONE': u'\033[0m',
        'OK': u'\033[94m',
        'INFO': u'\033[92m',
        'WARNING': u'\033[93m',
        'ERR': u'\033[91m',
        'FATAL': u'\033[31m',
        'ENDC': u'\033[0m'
    }

    def __init__(self, str):
        """
            Prints in white to stdout
        """
        print(str, file=sys.stdout)
        del self

    @staticmethod
    def ok(str):
        """
            Prints in blue to stdout
        """
        print(cprint.colors['OK'] + str + cprint.colors['ENDC'],
              file=sys.stdout)

    @staticmethod
    def info(str):
        """
            Prints in green to stdout
        """
        print(cprint.colors['INFO'] + str + cprint.colors['ENDC'],
              file=sys.stdout)

    @staticmethod
    def warn(str):
        """
            Prints in yellow to strerr
        """
        print(cprint.colors['WARNING'] + str + cprint.colors['ENDC'],
              file=sys.stderr)

    @staticmethod
    def err(str, interrupt=False):
        """
            Prints in brown to stderr
            interrupt=True: stops the program
        """
        print(cprint.colors['ERR'] + str + cprint.colors['ENDC'],
              file=sys.stderr)
        if interrupt:
            print(cprint.colors['ERR'] + "Error: Program stopped." +
                  cprint.colors['ENDC'],
                  file=sys.stderr)
            exit(1)

    @staticmethod
    def fatal(str, interrupt=False):
        """
            Prints in red to stderr
            interrupt=True: stops the program
        """
        print(cprint.colors['FATAL'] + str + cprint.colors['ENDC'],
              file=sys.stderr)
        if interrupt:
            print(cprint.colors['FATAL'] + "Fatal error: Program stopped." +
                  cprint.colors['ENDC'],
                  file=sys.stderr)
            exit(1)
