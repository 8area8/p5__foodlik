#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""User Interface."""

import os
from prompt_toolkit import prompt

from core.front.classes.title import TitleScreen


def init():
    """Launch the application in a loop."""
    running = True
    page = Interface()
    while running:

        page.show_content()

        action = prompt("type an action: ", completer=page.complete)

        if action in ("quit", "q"):
            print("good bye!")
            running = False
        elif action in page.actions:
            page.apply(action)
        else:
            page.add_action_error(action)


class Interface():
    """This class is the User Interface of the application.

    It uses a strategy pattern.
    Each strategy is a "page" that contains information to display.
    These "pages" show the layout of the web pages with three distinct parts:
        - a header
        - a content
        - a footer.

    self.section can contain differents classes and is used in "duck typing".
    """

    def __init__(self):
        """Initialization."""
        self.section = TitleScreen()

    @property
    def complete(self):
        """Get the autocompletion."""
        return self.section.auto_completion

    @property
    def actions(self):
        """Show the possibles actions."""
        return self.section.actions

    def show_content(self):
        """Display the current section."""
        clear()
        print(self.section)

    def apply(self, action):
        """Apply an action."""
        self.section.apply(action)

    def add_action_error(self, action):
        """Catch an error message."""
        self.section.add_action_error(action)


def clear():
    """Clear the console."""
    os.system('cls')
    os.system('clear')
