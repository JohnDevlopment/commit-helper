"""
`tagged` convention.
"""
from __future__ import annotations

def tagged_convention(tag: str, msg: str):
    # pylint: disable=missing-function-docstring
    tag = tag.upper()
    composed_message = f"{tag}: {msg}\n"
    return composed_message


TAGGED_CONVENTION_HELP = \
    """
    The tagged convention:

    TAG: message
    <BLANK>
    <body>
    <BLANK>
    <footer>

    ---
    Tag usage:

    ADD     -> use for new files or methods
    FEAT    -> for when adding a new feature
    DEL     -> use for excluded files or methods
    CHR     -> use for normal dev work and maintainance
    MERGE   -> use for signal merges
    DOCS    -> for documentation changes
    FIX     -> use for solving bugs or failures in file
    REF     -> use for when you rename a file
    STYLE   -> use for fixing stylesheet errors
    TEST    -> use for test files
    CI      -> for that commit that aims for fix a build
    """
