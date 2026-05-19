from typing import Optional
from sqlmodel import Field, SQLModel

class User(SQLModel, table=True):
    __tablename__ = "users"

    # table=True를 주면 DB 테이블이 되고, 생략하면 일반 Pydantic 스키마처럼 동작합니다.
    id: Optional[int] = Field(
        default=None, 
        primary_key=True, 
        alias="id"
    )
    userId: Optional[int] = Field(default=None, primary_key=True, alias="userId")
    name: str
    age: int

    class Config:
        # FastAPI 입출력 시 'userId'와 'id'가 유연하게 매핑되도록 설정
        populate_by_name = True