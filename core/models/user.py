# core/models/user.py
"""
Модель пользователя — основная сущность системы.
Связана с Telegram через telegram_id.
"""

from sqlalchemy import BigInteger, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional, List
from .base import Base  # Будет создан позже — общий Base


class User(Base):
    """
    SQLAlchemy модель пользователя.
    Использует аннотации Mapped[] — современный стиль SQLAlchemy 2.0+.
    """
    __tablename__ = "users"

    # === Поля ===
    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
        doc="Внутренний ID в БД (автоинкремент)"
    )
    
    telegram_id: Mapped[int] = mapped_column(
        BigInteger,
        unique=True,
        nullable=False,
        index=True,
        doc="Уникальный ID из Telegram API"
    )
    
    username: Mapped[Optional[str]] = mapped_column(
        String,
        nullable=True,
        doc="Юзернейм (@username), может измениться"
    )
    
    first_name: Mapped[Optional[str]] = mapped_column(
        String,
        nullable=True,
        doc="Имя пользователя"
    )
    
    last_name: Mapped[Optional[str]] = mapped_column(
        String,
        nullable=True,
        doc="Фамилия"
    )

    # === Связи (One-to-Many) ===
    dreams: Mapped[List["Dream"]] = relationship(
        "Dream",
        back_populates="user",
        cascade="all, delete-orphan",
        doc="Все сны пользователя"
    )
    
    diary_entries: Mapped[List["DiaryEntry"]] = relationship(
        "DiaryEntry",
        back_populates="user",
        cascade="all, delete-orphan",
        doc="Все записи дневника"
    )