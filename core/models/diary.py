# core/models/diary.py
"""
Запись повседневных событий.
Используется для анализа паттернов и связи со снами.
"""

from sqlalchemy import ForeignKey, Text, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from typing import Optional
from .base import Base
from .user import User


class DiaryEntry(Base):
    """
    Одна запись в дневнике.
    """
    __tablename__ = "diary_entries"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )
    
    date: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
        index=True
    )
    
    text: Mapped[str] = mapped_column(
        Text,
        nullable=False,
        doc="Что произошло за день"
    )
    
    analysis: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True,
        doc="Краткий анализ записи (опционально)"
    )

    user: Mapped[User] = relationship(
        "User",
        back_populates="diary_entries"
    )