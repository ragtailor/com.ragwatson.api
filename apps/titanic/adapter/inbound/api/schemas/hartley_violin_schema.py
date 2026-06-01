from pydantic import BaseModel


class ViolinEventResponse(BaseModel):
    playing: str
    status: str
