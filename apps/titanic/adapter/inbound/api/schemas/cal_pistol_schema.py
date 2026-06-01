from typing import Any

from pydantic import BaseModel


class PassengerValidationResponse(BaseModel):
    valid: bool
    passenger: dict[str, Any]
