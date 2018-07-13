#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""Globals functions."""


def section_repr(self):
    """Return a CLI representation."""
    return self.header + ("\n" * 2) + self.content + "\n" + self.footer


class BaseSection():
    """Abstract base for every sections."""

    def __init__(self):
        """Initialize the class."""

    def actions(self):
        """Return the possible actions."""
        raise NotImplementedError

    def apply(self):
        """Apply an action."""
        raise NotImplementedError

    def action_error(self, action):
        """Return an error text."""
        return (f"The action '{action}' is not a valid action.\n"
                f"Valid actions are {self.actions}.")


BaseSection.__str__ = section_repr  # monkey patching.
