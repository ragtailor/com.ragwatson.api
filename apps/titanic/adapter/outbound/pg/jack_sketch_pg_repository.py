from __future__ import annotations

from typing import Any

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from titanic.adapter.outbound.orm.titanic_model import TitanicRecord

_FEATURE_FIELDS = ["pclass", "gender", "age", "sibsp", "parch", "fare", "survived"]


class JackSketchPgRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_training_data(self) -> list[dict[str, Any]]:
        """생존 예측 모델 학습에 사용할 피처 데이터 조회"""
        rows = (
            await self.session.execute(select(TitanicRecord).order_by(TitanicRecord.id))
        ).scalars().all()
        return [{f: getattr(r, f) for f in _FEATURE_FIELDS} for r in rows]
