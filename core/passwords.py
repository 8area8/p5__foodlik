#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""Get the database user and passwords.

NOTE: I use environment variables for this:
Create an "app_env" file at the root of the project.
insert in:
"
export POSTGRES_USER="your_id"
export POSTGRES_PASSWORD="your_password"

export MYSQL_USER="your_id"
export MYSQL_PASSWORD="your_password"
"

Replacing the identifiers and passwords with yours.
Then start the file in your console ('source app_env' or '. App_env').
Environment variables will be loaded at each application launch,
which will save you from having to retype your username and password.

The name "app_env" is automatically ignored by Git.
"""

import os
import getpass


POSTGRES_USER = os.environ.get("POSTGRES_USER", '')
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD", '')

MYSQL_USER = os.environ.get("MYSQL_USER", '')
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD", '')

DB_CHOICE = ""
DB_USER = ""
DB_PASSWORD = ""


def init(args):
    """Initialize the ID recuperation.

    Dirty, but that was it or a class.
    """
    global POSTGRES_USER
    global POSTGRES_PASSWORD
    global MYSQL_USER
    global MYSQL_PASSWORD
    global DB_CHOICE
    global DB_USER
    global DB_PASSWORD

    if args["--postgres"]:
        DB_CHOICE = "postgres"
        DB_USER = POSTGRES_USER
        DB_PASSWORD = POSTGRES_PASSWORD
        if not DB_USER:
            DB_USER = input("postgres user: ")
        if not DB_PASSWORD:
            DB_PASSWORD = getpass.getpass("PostgreSQL password:")

    elif args["--mysql"]:
        DB_CHOICE = "mysql"
        DB_USER = MYSQL_USER
        DB_PASSWORD = MYSQL_PASSWORD
        if not DB_USER:
            DB_USER = input("MySQL user: ")
        if not DB_PASSWORD:
            DB_PASSWORD = getpass.getpass("MySQL password (invisible):")
