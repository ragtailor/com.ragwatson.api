from pydantic import BaseModel


class BlueprintResponse(BaseModel):
    ship: str
    columns: list[str]
