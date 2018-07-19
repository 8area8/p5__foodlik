#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""Starts the FoodLik program or follows the data instructions provided.

Usage:
    main.py (--msql | --psql)
    main.py (-l | --load_pages) [FIRST-PAGE [to LAST-PAGE]]
    main.py (--msql | --psql) (-c | --create_database)
    main.py (--msql | --psql) (-f | --full_install) [FIRST-PAGE [to LAST-PAGE]]
    main.py (-h | --help)
    main.py --version


Arguments:
    FIRST-PAGE      First page to load. Needs load_datas. [default: 1]
    LAST-PAGE       Last page to load. Needs load_datas and FIRST-PAGE.


Options:
    -h --help               Show this screen.
    -l --load_pages         load the datas from the OpenFoodFact web API.
    -c --create_database    (Re)create all the database.
    -f --full_install       Compile --load_pages and --create_database.
    --psql                  Use the PostgreSQL server.
    --msql                  Use the MySQL server.
    --version               Show version.

"""

from docopt import docopt

import core.passwords as passwords
import core.back.requests.load_pages as load_pages
import core.back.database.create_database as create_database
import core.front.user_interface as user_interface
from core.back.database.data_wrapper import datas_wrapper


def main():
    """Core function."""
    arguments = docopt(__doc__, version='1.0')

    passwords.init(arguments)

    if arguments["--load_pages"]:
        first_p = max(arguments["FIRST-PAGE"], 1, key=bool)
        last_p = max(arguments["LAST-PAGE"], 30, key=bool)
        load_pages.init(first_p, last_p)

    elif arguments["--create_database"]:
        create_database.init()

    elif arguments["--full_install"]:
        first_p = max(arguments["FIRST-PAGE"], 1, key=bool)
        last_p = max(arguments["LAST-PAGE"], 30, key=bool)
        load_pages.init(first_p, last_p)
        create_database.init()

    elif arguments["--msql"] or arguments["--psql"]:
        datas_wrapper.connect()  # Needed after the ID initialization.
        user_interface.init()

    else:
        print("main.py: Argument error.")


if __name__ == "__main__":
    main()
