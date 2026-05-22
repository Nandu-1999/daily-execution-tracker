from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.db.dependencies import get_db
from app.models.user import User
from app.core.security import (
    oauth2_scheme,
    verify_access_token
)


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):

    payload = verify_access_token(token)

    if not payload:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )

    user_id = payload.get("sub")

    statement = select(User).where(
        User.id == user_id
    )

    user = db.execute(
        statement
    ).scalar_one_or_none()

    if not user:
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )

    return user