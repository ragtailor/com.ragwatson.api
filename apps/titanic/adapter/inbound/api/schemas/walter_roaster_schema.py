from typing import Optional

from pydantic import BaseModel


class PassengerResponse(BaseModel):
    id: int
    passenger: Optional[str] = None
    survived: Optional[str] = None
    pclass: Optional[str] = None
    name: Optional[str] = None
    gender: Optional[str] = None
    age: Optional[str] = None
    sibsp: Optional[str] = None
    parch: Optional[str] = None
    ticket: Optional[str] = None
    fare: Optional[str] = None
    cabin: Optional[str] = None
    embarked: Optional[str] = None


class PaginatedPassengersResponse(BaseModel):
    total: int
    page: int
    page_size: int
    items: list[PassengerResponse]
