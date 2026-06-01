from pydantic import BaseModel


class CoupleSurvivalResponse(BaseModel):
    husband: str
    wife: str
    message: str
