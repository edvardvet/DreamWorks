# core/models/pattern.py
"""
Паттерны поведения, выявленные ИИ.
Например: 'work_frustration' — 5 раз за месяц.
"""

from sqlalchemy import ForeignKey, String, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from .base import Base


class Pattern(Base):
    """
    Повторяющийся паттерн в дневнике.
    """
    __tablename__ = "patterns"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
        index=True
    )
    
    type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        index=True,
        doc="Тип: work_frustration, anxiety, etc."
    )
    
    description: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
        doc="Подробное описание от ИИ"
    )
    
    count: Mapped[int] = mapped_column(
        Integer,
        default=1,
        doc="Сколько раз встретился"
    )
    
    last_seen: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        doc="Когда последний раз обновлялся"
    )