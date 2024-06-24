from __future__ import annotations
from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from typing import Any

class ConfigFile(Protocol):
    def __getitem__(self, key: str) -> Any:
        ...
