from fastapi import APIRouter
from titanic.app.use_cases.caledon_query import CaledonValidation

'''
잭 도슨 (Jack Dawson)
자유로운 영혼, 예술가, 그리고 로즈를 구원하는 인물인 만큼
'그림'이나 '포커 도박'과 관련된 키워드가 잘 어울립니다.
생존 예측 모델의 핵심 인터페이스를 담당합니다.
'''

jack_sketch_router = APIRouter(prefix="/titanic/jack", tags=["jack"])


@jack_sketch_router.get("/sketch")
async def analyze_jack_dawson():
    """잭 도슨 생존 분석 (3등석 남성의 생존 가능성)"""
    pass


@jack_sketch_router.get("/model")
async def get_model_info():
    """학습된 생존 예측 모델 정보 조회"""
    pass


@jack_sketch_router.post("/predict")
async def predict_survival(passenger: CaledonValidation):
    """승객 정보를 입력받아 생존 확률 예측"""
    pass
