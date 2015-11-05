# coding: utf8
from cprint import *

def p(str):
    print(str)
    cprint(str)
    cprint.ok(str)
    cprint.info(str)
    cprint.warn(str)
    cprint.err(str)
    cprint.fatal(str)

if __name__ == '__main__':
    p("simple1")
    p(u"simple2'''&é'((-è__çà)==)^^¨¨")
