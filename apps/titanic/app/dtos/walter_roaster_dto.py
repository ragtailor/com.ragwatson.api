from dataclasses import dataclass, field
from typing import Any


@dataclass
class WalterPaginationDTO:
    page: int
    page_size: int


@dataclass
class WalterPassengerListDTO:
    total: int
    page: int
    page_size: int
    items: list[dict[str, Any]] = field(default_factory=list)
