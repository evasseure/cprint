# coding: utf8
from cprint import *
import pytest


class TestClass(object):
    def __init__(self):
        self.name = "Joe"
    def __repr__(self):
        return self.name

def p(str):
    print(str)
    cprint(str)
    cprint.ok(str)
    cprint.info(str)
    cprint.warn(str)
    cprint.err(str)
    cprint.fatal(str)


def test_simple_print():
    """ Testing cprint with simple string. """
    p("simple1")
    return


def test_hard_print():
    """ Testing cprint with ugly string. """
    p(u"simple2'''&é'((-è__çà)==)^^¨¨")
    return


def test_print_int():
    """ Testing cprint with int. """
    p(1)
    return


def test_print_int_list():
    """ Testing cprint with int list. """
    p([1, 2, 3, 4])
    return


def test_print_list():
    """ Testing cprint with list. """
    p(['l1', 'l2', 'l3'])
    return


def test_print_tuple():
    """ Testing cprint with tuple. """
    p(('t1', 't2', 't3'))
    return

def test_print_tuple():
    """ Testing cprint with tuple. """
    p(('t1', 't2', 't3'))
    return

def test_print_object():
    """ Testing cprint with object. """
    o = TestClass()
    p(o)
    return