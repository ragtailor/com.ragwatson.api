from dataclasses import dataclass, field
from typing import Any


@dataclass
class JamesUploadDTO:
    records: list[dict[str, Any]] = field(default_factory=list)


@dataclass
class JamesSaveResultDTO:
    saved: int
