from typing import Any, Optional

from pydantic import BaseModel


class ModelInfoResponse(BaseModel):
    model_name: str
    train_accuracy: str


class SurvivalPredictionResponse(BaseModel):
    survived: int
    survival_probability: str
    death_probability: str
    passenger_info: dict[str, Any]
    message: Optional[str] = None
    analysis: Optional[str] = None
