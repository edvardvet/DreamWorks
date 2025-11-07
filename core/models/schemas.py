# core/models/schemas.py
"""
Pydantic схемы для валидации и сериализации.
Отдельный файл — чистая архитектура.
"""

from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class UserCreate(BaseModel):
    telegram_id: int
    username: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None


class UserRead(BaseModel):
    id: int
    telegram_id: int
    username: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]

    class Config:
        from_attributes = True


class DreamCreate(BaseModel):
    text: str


class DreamRead(BaseModel):
    id: int
    date: datetime
    text: str
    interpretation: Optional[str] = None

    class Config:
        from_attributes = True


class DiaryCreate(BaseModel):
    text: str


class DiaryRead(BaseModel):
    id: int
    date: datetime
    text: str
    analysis: Optional[str] = None

    class Config:
        from_attributes = True


class PatternRead(BaseModel):
    id: int
    type: str
    description: str
    count: int
    last_seen: datetime

    class Config:
        from_attributes = True