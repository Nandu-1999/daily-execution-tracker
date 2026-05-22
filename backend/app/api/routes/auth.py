from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.db.dependencies import get_db
from app.schemas.user import UserCreate
from app.schemas.user import UserLogin
from app.models.user import User
from app.core.security import hash_password
from app.core.security import (
    verify_password,
    create_access_token
)

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/register")
def register_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    new_user = User(
        name=user.name,
        email=user.email,
        password_hash=hash_password(user.password)
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    return {
        "message": "User created successfully"
    }

@router.post("/login")
def login_user(
    user: UserLogin,
    db: Session = Depends(get_db)
):

    statement = select(User).where(
        User.email == user.email
    )

    existing_user = db.execute(
        statement
    ).scalar_one_or_none()

    if not existing_user:
        return {
            "message": "Invalid credentials"
        }

    is_valid_password = verify_password(
        user.password,
        existing_user.password_hash
    )

    if not is_valid_password:
        return {
            "message": "Invalid credentials"
        }

    access_token = create_access_token({
        "sub": str(existing_user.id)
    })

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }