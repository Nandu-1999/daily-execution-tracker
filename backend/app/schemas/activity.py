from datetime import date
from uuid import UUID

from pydantic import (
    BaseModel,
    field_validator
)

from app.models.activity_category import (
    ActivityCategory
)


class ActivityCreate(BaseModel):

    title: str

    category: ActivityCategory

    duration_minutes: int

    activity_date: date

    notes: str | None = None

    @field_validator("title")
    @classmethod
    def validate_title(cls, value):

        if not value.strip():
            raise ValueError(
                "Title cannot be empty"
            )

        return value.strip()

    @field_validator("duration_minutes")
    @classmethod
    def validate_duration(cls, value):

        if value <= 0:
            raise ValueError(
                "Duration must be greater than 0"
            )

        return value


class ActivityResponse(BaseModel):

    id: UUID

    title: str

    category: ActivityCategory

    duration_minutes: int

    activity_date: date

    notes: str | None

    class Config:
        from_attributes = True