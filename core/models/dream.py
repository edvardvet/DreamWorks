# core/models/dream.py
"""
Модель сна — основная единица для анализа.
Содержит текст и интерпретацию (заполняется ИИ).
"""

from sqlalchemy import ForeignKey, Text, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from typing import Optional
from .base import Base
from .user import User


class Dream(Base):
    """
    Сон пользователя.
    Принадлежит одному пользователю.
    """
    __tablename__ = "dreams"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
        doc="Ссылка на пользователя"
    )
    
    date: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
        index=True,
        doc="Дата и время записи (UTC)"
    )
    
    text: Mapped[str] = mapped_column(
        Text,
        nullable=False,
        doc="Текст сна (от пользователя)"
    )
    
    interpretation: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True,
        doc="Толкование по Юнгу (заполняется ИИ)"
    )

    # === Обратная связь ===
    user: Mapped[User] = relationship(
        "User",
        back_populates="dreams",
        doc="Автор сна"
    )