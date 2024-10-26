"""
Protocols.
"""
from __future__ import annotations
from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from typing import Any

class ConfigFile(Protocol):
    # pylint: disable=missing-class-docstring,too-few-public-methods
    def __getitem__(self, key: str) -> Any:
        # pylint: disable=missing-function-docstring
        ...
