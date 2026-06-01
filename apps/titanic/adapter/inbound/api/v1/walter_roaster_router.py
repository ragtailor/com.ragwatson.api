from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_db
from titanic.adapter.outbound.pg.walter_pg_repository import WalterPgRepository
from titanic.app.use_cases.walter_query import WalterQuery

'''
영화 <타이타닉>에서 승객 명단을 관리하는 
일등 항해사 윌터 와일딩(Walter Nichols / 혹은 윌리엄 머독 등 영화 속 관리자 캐릭터) 
또는 승객 명단(Passenger List)을 다루는 '월터'라는 인물의 상황에 맞추어, 
직관적이면서도 센스 있는 중간 키워드를 추천해 드립니다.
'''

walter_router = APIRouter(prefix="/titanic/walter", tags=["walter"])


@walter_router.get("/passengers")
async def list_passengers(
    page: int = Query(default=1, ge=1),
    page_size: int = Query(default=50, ge=1, le=200),
    db: AsyncSession = Depends(get_db),
):
    repository = WalterPgRepository(db)
    use_case = WalterQuery(repository)
    return await use_case.list_paginated(page, page_size)
