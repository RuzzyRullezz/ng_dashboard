from dataclasses import dataclass
from typing import Union, Type

from sqlalchemy.orm import Session

from ..models import UserTypeEnum
from .models import ProfileClient, ProfileExecutor, ProfileType


@dataclass
class ProfileBaseData:
    first_name: str
    last_name: str
    country: str
    phone: str


@dataclass
class ProfileExecutorData(ProfileBaseData):
    # TODO: заполнить полями заказчика
    ...


@dataclass
class ProfileClientData(ProfileBaseData):
    # TODO: заполнить полями исполнителя
    ...


def get_profile_data_cls(user_type: UserTypeEnum) -> Union[Type[ProfileClientData], Type[ProfileExecutorData]]:
    if user_type == UserTypeEnum.client:
        return ProfileClientData
    elif user_type == UserTypeEnum.executor:
        return ProfileExecutorData
    else:
        raise NotImplementedError(f"Unsupported user_type = {user_type}")


ProfileDataType = Union[ProfileExecutorData, ProfileClientData]


def create_client_profile(
        db_session: Session,
        user_id: int,
        profile_client_data: ProfileClientData) -> ProfileClient:
    profile = ProfileClient(
        user_id=user_id,
        first_name=profile_client_data.first_name,
        last_name=profile_client_data.last_name,
        country=profile_client_data.country,
        phone=profile_client_data.phone,
    )
    db_session.add(profile)
    db_session.flush()
    db_session.refresh(profile)
    return profile


def create_executor_profile(
        db_session: Session,
        user_id: int,
        profile_executor_data: ProfileExecutorData) -> ProfileExecutor:
    profile = ProfileExecutor(
        user_id=user_id,
        first_name=profile_executor_data.first_name,
        last_name=profile_executor_data.last_name,
        country=profile_executor_data.country,
        phone=profile_executor_data.phone,
    )
    db_session.add(profile)
    db_session.flush()
    db_session.refresh(profile)
    return profile


def create_profile(
        db_session: Session,
        user_id: int,
        user_type: UserTypeEnum,
        profile_data: ProfileDataType) -> ProfileType:
    if user_type == UserTypeEnum.executor:
        assert isinstance(profile_data, ProfileExecutorData)
    elif user_type == UserTypeEnum.client:
        assert isinstance(profile_data, ProfileClientData)
    else:
        raise AssertionError("Unreachable statement")
    if isinstance(profile_data, ProfileClientData):
        return create_client_profile(db_session, user_id, profile_data)
    elif isinstance(profile_data, ProfileExecutorData):
        return create_executor_profile(db_session, user_id, profile_data)
    else:
        raise NotImplementedError(f"Unsupported profile_data type {type(profile_data)}")
