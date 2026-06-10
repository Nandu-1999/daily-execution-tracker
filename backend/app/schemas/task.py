from pydantic import BaseModel
from uuid import UUID


from pydantic import BaseModel,Field, field_validator

class TaskCreate(BaseModel):
    title: str
    description: str | None = None

    title: str = Field(max_length=255)

    @field_validator("title")
    @classmethod
    def validate_title(cls, value):
        if not value.strip():
            raise ValueError(
                "Title cannot be empty or whitespace"
            )

        return value.strip()


class TaskResponse(BaseModel):
    id: UUID
    title: str
    description: str | None
    is_completed: bool

    class Config:
        from_attributes = True