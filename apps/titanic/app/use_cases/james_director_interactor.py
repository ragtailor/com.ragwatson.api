from __future__ import annotations

from typing import Any

from titanic.app.ports.input.james_director_use_case import JamesDirectorUseCase
from titanic.app.ports.output.james_repository import JamesRepository


class JamesDirectorInteractor(JamesDirectorUseCase):
    def __init__(self, repository: JamesRepository) -> None:
        self._repository = repository

    async def receive_uploaded_records(self, records: list[dict[str, Any]]) -> dict[str, Any]:
        count = await self._repository.save_all(records)
        return {"saved": count}

