from pydantic import BaseModel


class PassengerStatsResponse(BaseModel):
    total: int
    survived: int
    perished: int
