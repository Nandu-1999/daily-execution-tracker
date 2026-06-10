from pydantic import BaseModel


class DailySummaryResponse(BaseModel):

    total_minutes: int

    upskilling_minutes: int

    work_minutes: int

    exercise_minutes: int

    research_minutes: int

    personal_minutes: int