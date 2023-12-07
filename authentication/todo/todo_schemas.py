from pydantic import BaseModel, Field


class Todo(BaseModel):
    title: str = Field(min_length=3)
    description: str
    complete: bool = False
