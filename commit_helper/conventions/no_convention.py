"""
No convention.
"""
from __future__ import annotations
from ..utils.colors import INPUT_COLOR, RESET

def just_message(msg: str=""):
    # pylint: disable=missing-function-docstring
    if msg == '':
        message = str(input(INPUT_COLOR + "commit message: " + RESET))
    else:
        message = msg

    composed = "%s\n" % message.capitalize()
    return composed
