import uuid

from sqlalchemy import (
    Column,
    String,
    Integer,
    Date,
    DateTime,
    ForeignKey,
    Enum
)

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.db.database import Base
from app.models.activity_category import ActivityCategory


class Activity(Base):

    __tablename__ = "activities"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    title = Column(
        String(255),
        nullable=False
    )

    category = Column(
        Enum(ActivityCategory),
        nullable=False
    )

    duration_minutes = Column(
        Integer,
        nullable=False
    )

    activity_date = Column(
        Date,
        nullable=False
    )

    notes = Column(
        String,
        nullable=True
    )

    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    user = relationship("User")