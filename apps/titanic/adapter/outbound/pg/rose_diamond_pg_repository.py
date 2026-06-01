from __future__ import annotations

from typing import Any

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from titanic.adapter.outbound.orm.titanic_model import TitanicRecord

_ROW_FIELDS = [
    "id", "passenger", "survived", "pclass", "name", "gender",
    "age", "sibsp", "parch", "ticket", "fare", "cabin", "embarked",
]


class RoseDiamondPgRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_all_records(self) -> list[dict[str, Any]]:
        """ML 학습에 사용할 전체 승객 데이터 조회"""
        rows = (
            await self.session.execute(select(TitanicRecord).order_by(TitanicRecord.id))
        ).scalars().all()
        return [{f: getattr(r, f) for f in _ROW_FIELDS} for r in rows]
