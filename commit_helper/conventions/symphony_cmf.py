"""
`symphony` convention.
"""
from __future__ import annotations

def symphony_convention(tag: str, msg: str):
    # pylint: disable=missing-function-docstring
    tag = tag.capitalize()
    composed = f"[{tag}] {msg}\n"
    return composed

SYMPHONY_CONVENTION_HELP = \
    """
    The symphony CMF convention:

    [<Tag>] <message>
    <BLANK>
    <body>
    <BLANK>
    <changes>
    <BLANK>
    <footer>

    ---
    Obs.:
    Tag is not a tag similar to other commit conventions, it is actually a
    context to what was changed.

    ---
    Optionals:
    <body>, <changes>, <footer>
    """
