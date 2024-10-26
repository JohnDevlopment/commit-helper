from __future__ import annotations

def john_convention(tag: str, msg: str, context: str) -> str:
    tag = tag.upper()
    context = context.capitalize()
    if not context:
        return f"[{tag}] {msg}"
    return f"[{tag}] {context}: {msg}"

JOHN_CONVENTION_HELP = \
        """
        The john convention:

        [<tag>] <scope>: <message>
        <BLANK>
        <body>
        <BLANK>
        <footer>

        ----
        Tags:
        ADD:		Adding files
        FIX:		Fixing a bug
        FEATURE:	Changes that amount to adding a new feature
        PROJECT:	Changes that affect the project itself or its build system
        REFACTOR:	Changing the look of code but not its actual behavior
        REMOVE:		Removing files
        UPDATE:		Updating files

        ----
        Optional fields:
        Every field except <message> and <tag>
        """
