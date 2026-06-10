from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session
from sqlalchemy import select

from app.db.dependencies import get_db

from app.models.activity import Activity
from app.models.user import User
from datetime import date
from app.schemas.activity_summary import DailySummaryResponse
from app.models.activity_category import ActivityCategory

from app.schemas.activity import (
    ActivityCreate,
    ActivityResponse
)

from app.api.dependencies.auth import (
    get_current_user
)

router = APIRouter(
    prefix="/activities",
    tags=["Activities"]
)

@router.post(
    "",
    response_model=ActivityResponse
)
def create_activity(
    activity: ActivityCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    new_activity = Activity(
        title=activity.title,
        category=activity.category,
        duration_minutes=activity.duration_minutes,
        activity_date=activity.activity_date,
        notes=activity.notes,
        user_id=current_user.id
    )

    db.add(new_activity)

    db.commit()

    db.refresh(new_activity)

    return new_activity

@router.get(
    "",
    response_model=list[ActivityResponse]
)
def get_activities(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    statement = select(Activity).where(
        Activity.user_id == current_user.id
    )

    activities = db.execute(
        statement
    ).scalars().all()

    return activities

@router.get(
    "/summary/today",
    response_model=DailySummaryResponse
)
def get_today_summary(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    today = date.today()

    statement = select(Activity).where(
        Activity.user_id == current_user.id,
        Activity.activity_date == today
    )

    activities = db.execute(
        statement
    ).scalars().all()
    

    summary = {
        "total_minutes": 0,
        "upskilling_minutes": 0,
        "work_minutes": 0,
        "exercise_minutes": 0,
        "research_minutes": 0,
        "personal_minutes": 0
    }

    for activity in activities:

        summary["total_minutes"] += activity.duration_minutes

        if activity.category == ActivityCategory.UPSKILLING:
            summary["upskilling_minutes"] += activity.duration_minutes

        elif activity.category == ActivityCategory.WORK:
            summary["work_minutes"] += activity.duration_minutes

        elif activity.category == ActivityCategory.EXERCISE:
            summary["exercise_minutes"] += activity.duration_minutes

        elif activity.category == ActivityCategory.RESEARCH:
            summary["research_minutes"] += activity.duration_minutes

        elif activity.category == ActivityCategory.PERSONAL:
            summary["personal_minutes"] += activity.duration_minutes

    return summary

@router.get(
    "/summary/date/{activity_date}",
    response_model=DailySummaryResponse
)
def get_summary_by_date(
    activity_date: date,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    Activity.activity_date == activity_date
    
    statement = select(Activity).where(
    Activity.user_id == current_user.id,
    Activity.activity_date == activity_date
)
    activities = db.execute(
        statement
    ).scalars().all()
    

    summary = {
        "total_minutes": 0,
        "upskilling_minutes": 0,
        "work_minutes": 0,
        "exercise_minutes": 0,
        "research_minutes": 0,
        "personal_minutes": 0
    }

    for activity in activities:

        summary["total_minutes"] += activity.duration_minutes

        if activity.category == ActivityCategory.UPSKILLING:
            summary["upskilling_minutes"] += activity.duration_minutes

        elif activity.category == ActivityCategory.WORK:
            summary["work_minutes"] += activity.duration_minutes

        elif activity.category == ActivityCategory.EXERCISE:
            summary["exercise_minutes"] += activity.duration_minutes

        elif activity.category == ActivityCategory.RESEARCH:
            summary["research_minutes"] += activity.duration_minutes

        elif activity.category == ActivityCategory.PERSONAL:
            summary["personal_minutes"] += activity.duration_minutes

    return summary