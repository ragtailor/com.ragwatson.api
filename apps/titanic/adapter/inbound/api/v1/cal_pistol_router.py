from fastapi import APIRouter
from titanic.app.use_cases.caledon_query import CaledonValidation

'''
칼 캘던 하클리 (Caledon Hockley)
오만하고 부유한 자산가이자, 소유욕이 강하고 빌런으로서의
면모를 드러내는 키워드입니다.
승객 입력값 유효성 검사를 담당합니다.
'''

cal_pistol_router = APIRouter(prefix="/titanic/cal", tags=["cal"])


@cal_pistol_router.post("/pistol")
async def validate_passenger(passenger: CaledonValidation):
    """승객 데이터 유효성 검사"""
    return {"valid": True, "passenger": passenger.model_dump()}
