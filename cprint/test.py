from cprint import *

if __name__ == '__main__':
    print("print(str)")
    cprint('cprint(str)')
    cprint.ok("cprint.ok(str)")
    cprint.info("cprint.info(str)")
    cprint.warn("cprint.warn(str)")
    cprint.err("cprint.err(str)")
    cprint.fatal("cprint.fatal(str)")
    cprint.fatal("cprint.fatal(str, interrupt=True)", True)