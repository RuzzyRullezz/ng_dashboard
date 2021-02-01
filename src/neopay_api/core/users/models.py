from __future__ import annotations

from enum import Enum
from sqlalchemy import Column, BigInteger, DateTime, Unicode, func, Enum as SAEnum

from neopay_api.db import Base


class UserTypeEnum(str, Enum):
    client = 'client'
    executor = 'executor'


class User(Base):
    __tablename__ = 'user'
    id = Column(BigInteger(), primary_key=True, nullable=False)
    login = Column(Unicode(), index=True, unique=True, nullable=False)
    hashed_password = Column(Unicode(), index=True, nullable=False)
    type = Column(SAEnum(UserTypeEnum, native_enum=False), index=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
