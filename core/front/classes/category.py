#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""Category section."""

from termcolor import colored

from core.front.classes.globals import BaseSection
from core.back.database.data_wrapper import datas_wrapper as datas


class Category(BaseSection):
    """The Category class."""

    def __init__(self):
        """Initialization."""
        super().__init__()

        self.page = 1
        self.max_pages = datas.len_category // 15
        self.current_category = []

        # FOOTER COMMANDS
        self.c_next = "[n] or [next]: go to the next page.\n"
        self.c_bef = "[b] or [before]: go to the previous page.\n"
        self.c_page = "[number] keyword: go to the corresponding page.\n"
        self.c_ctg = "[categorie_name] keyword: go to the categorie page.\n"
