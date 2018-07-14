#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""Title screen."""

from datetime import datetime

from termcolor import colored

from core.front.classes.globals import BaseSection


TITLE = """
    oooooooooooo                           .o8  oooo   o8o  oooo   COPYRIGHT
    '888'     '8                          "888  '888   '"'  `888
     888          .ooooo.   .ooooo.   .oooo888   888  oooo   888  oooo
     888oooo8    d88' '88b d88' '88b d88' '888   888  `888   888 .8P'
     888    "    888   888 888   888 888   888   888   888   888888.
     888         888   888 888   888 888   888   888   888   888 `88b.
    o888o        'Y8bod8P' 'Y8bod8P' `Y8bod88P" o888o o888o o888o o888o"""


class TitleScreen(BaseSection):
    """This class show the title screen of the application."""

    def __init__(self):
        """Initialization."""
        super().__init__()

        self.c_enter = "\n[ENTER] keyword: go to categories."

        url = 'https://github.com/8area8/P4_OpenFoodFact_interface'
        version = "version 0.2"

        self.header = (f"Foodlik {version} "
                       f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}."
                       f"\nDocumentation available at {colored(url, 'cyan')}."
                       + "\n" * 2 + colored(TITLE, "green") + "\n" * 3 +
                       colored("Welcome to Foodlik !", "yellow") +
                       "\n" + colored("-" * 20, "yellow"))  # YOLO.

    @property
    def content(self):
        """Return the content informations."""
        return f"Simply type {colored('ENTER', 'green')} to begin." + "\n" * 2

    @property
    def footer(self):
        """Return the footer informations.

        Call 'Super().footer' to get the error messages.
        """
        text = self.comm + self.c_quit + self.c_enter + '\n' * 2
        text += colored(super().footer, "red")
        return text

    @property
    def actions(self):
        """Return the possible actions."""
        return "ENTER keyword, " + super().actions

    def apply(self, action):
        """Apply an action."""
        pass
