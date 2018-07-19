#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""User Interface main file."""

import os
from importlib import import_module

from prompt_toolkit import prompt

from core.front.classes.titlescreen import TitleScreen


def init():
    """Launch the application in a loop."""
    running = True
    page = Interface()
    while running:

        page.change_section()
        page.show_content()

        action = prompt("tapez une action: ", completer=page.complete)

        if action in ("quitter", "q"):
            print("au revoir!")
            page.close_connection()
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

    def change_section(self):
        """Replace the current section by another if needed.

        NOTE: I did not secure this code. be carrefull with self.change_to !
        """
        new_section = self.section.change_to
        if new_section:
            path = f"core.front.classes.{new_section.lower()}"
            self.section = getattr(import_module(path), new_section)()

    def close_connection(self):
        """Close the database connection."""
        return self.section.close_connection()


def clear():
    """Clear the console."""
    os.system('cls')
    os.system('clear')
