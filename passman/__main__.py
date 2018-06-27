#!/usr/bin/env python3

from passman import *

def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    initialize()
    check_users()
    login()
    menu_loop()

if __name__ == "__main__":
    main()