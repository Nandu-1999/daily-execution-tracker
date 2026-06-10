from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session
from typing import List
from sqlalchemy import select
from uuid import UUID
from fastapi import HTTPException

from app.db.dependencies import get_db
from app.models.task import Task
from app.models.user import User
from app.schemas.task import (
    TaskCreate,
    TaskResponse
)

from app.api.dependencies.auth import (
    get_current_user
)

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

@router.post(
    "",
    response_model=TaskResponse
)
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    new_task = Task(
        title=task.title,
        description=task.description,
        user_id=current_user.id
    )

    db.add(new_task)

    db.commit()

    db.refresh(new_task)

    return new_task

@router.get(
    "",
    response_model=list[TaskResponse]
)
def get_tasks(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    statement = select(Task).where(
        Task.user_id == current_user.id
    )

    tasks = db.execute(
        statement
    ).scalars().all()

    return tasks

@router.patch("/{task_id}/complete", response_model=TaskResponse)
def complete_task(
    task_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    statement = select(Task).where(
        Task.id == task_id
    )

    task = db.execute(
        statement
    ).scalar_one_or_none()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    if task.user_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="Not allowed"
        )

    task.is_completed = True

    db.commit()

    db.refresh(task)

    return task

@router.delete("/{task_id}")
def delete_task(
    task_id: UUID,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    statement = select(Task).where(
        Task.id == task_id
    )

    task = db.execute(
        statement
    ).scalar_one_or_none()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    if task.user_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="Not allowed"
        )

    db.delete(task)

    db.commit()

    return {
        "message": "Task deleted successfully"
    }