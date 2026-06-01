from __future__ import annotations

from typing import Any

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from titanic.adapter.outbound.orm.titanic_model import TitanicRecord

_ROW_FIELDS = [
    "id", "passenger", "survived", "pclass", "name", "gender",
    "age", "sibsp", "parch", "ticket", "fare", "cabin", "embarked",
]


class RuthCorsetPgRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def list_by_pclass(
        self, pclass: int, page: int, page_size: int
    ) -> tuple[int, list[dict[str, Any]]]:
        """등급(pclass)으로 필터링한 승객 목록 페이지네이션 조회"""
        pclass_str = str(pclass)
        total = (
            await self.session.execute(
                select(func.count())
                .select_from(TitanicRecord)
                .where(TitanicRecord.pclass == pclass_str)
            )
        ).scalar_one()
        rows = (
            await self.session.execute(
                select(TitanicRecord)
                .where(TitanicRecord.pclass == pclass_str)
                .order_by(TitanicRecord.id)
                .offset((page - 1) * page_size)
                .limit(page_size)
            )
        ).scalars().all()
        items = [{f: getattr(r, f) for f in _ROW_FIELDS} for r in rows]
        return total, items
