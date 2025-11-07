# core/models/base.py
"""
Общий базовый класс для всех моделей.
Позволяет использовать один Base.metadata.create_all()
"""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    Базовый класс для всех моделей.
    Наследуем от DeclarativeBase — SQLAlchemy 2.0+ стиль.
    """
    pass