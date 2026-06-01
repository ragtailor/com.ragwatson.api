from pydantic import BaseModel

from titanic.adapter.inbound.api.schemas.jack_sketch_schema import SurvivalPredictionResponse
from titanic.adapter.inbound.api.schemas.walter_roaster_schema import PaginatedPassengersResponse

__all__ = ["SurvivalPredictionResponse", "PaginatedPassengersResponse"]


class RoseSurvivalAnalysisResponse(SurvivalPredictionResponse):
    """로즈 드윗 부카터 생존 분석 결과 (SurvivalPredictionResponse 확장)"""
