from __future__ import annotations

from typing import Union

from sqlalchemy import Column, BigInteger, Unicode, ForeignKey
from sqlalchemy.orm import declared_attr

from neopay_api.db import Base


class ProfileBase:
    id = Column(BigInteger(), primary_key=True, nullable=False)
    first_name = Column(Unicode(), index=True, nullable=False)
    last_name = Column(Unicode(), index=True, nullable=False)
    country = Column(Unicode(), index=True, nullable=False)
    phone = Column(Unicode(), index=True, nullable=False)

    @declared_attr
    def user_id(cls):
        return Column(BigInteger(), ForeignKey('user.id', ondelete='CASCADE'), unique=True, nullable=False)


class ProfileClient(Base, ProfileBase):
    __tablename__ = 'profile_client'
    # TODO: заполнить полями заказчика


class ProfileExecutor(Base, ProfileBase):
    __tablename__ = 'profile_executor'
    # TODO: заполнить полями исполнителя


ProfileType = Union[ProfileClient, ProfileExecutor]