#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""Starts the FoodLik program or follows the data instructions provided.

Usage:
    main.py
    main.py load_pages [FIRST-PAGE [to LAST-PAGE]]
    main.py create_database
    main.py fill_in_database
    main.py --admin
    main.py (-h | --help)
    main.py --version


Arguments:
    FIRST-PAGE      First page to load. Needs load_datas. [default: 1]
    LAST-PAGE       Last page to load. Needs load_datas and FIRST-PAGE.


Options:
    -h --help       Show this screen.
    --version       Show version.
    --admin         Launch the administrator interface.

"""

from docopt import docopt

import core.back.requests.load_pages as load_pages


def main():
    """Core function."""
    arguments = docopt(__doc__, version='0.1')

    if arguments["load_pages"]:
        first_p = arguments["FIRST-PAGE"]
        last_p = arguments["LAST-PAGE"]
        load_pages.init(first_p, last_p)

    elif arguments["fill_in_database"]:
        fill_in.init()

    elif arguments["--admin"]:
        admin.init()

    elif not any(arguments.values()):
        user_interface.init()

    else:
        print("Argument error.")


if __name__ == "__main__":
    main()
