import uuid
from typing import Optional

from pydantic import BaseModel, Field


class TaskModel(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)
    completed: bool = False

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "id": "00010203-0405-0607-0809-0a0b0c0d0e0f",
                "name": "My important task",
                "completed": False,
            }
        }


class UpdateTaskModel(BaseModel):
    name: Optional[str]
    completed: Optional[bool]

    class Config:
        json_schema_extra = {
            "example": {
                "name": "My other important task",
                "completed": True,
            }
        }
