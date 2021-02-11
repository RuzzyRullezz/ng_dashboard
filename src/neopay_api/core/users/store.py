from dataclasses import dataclass
from typing import Optional

from neopay_api.core.users.exceptions import UserAlreadyExistsException
from sqlalchemy.orm import Session

from .models import User, UserTypeEnum
from .auth import get_password_hash
from .profiles.store import create_profile, ProfileDataType


def get_user_by_login(db_session: Session, login: str) -> Optional[User]:
    user = db_session.query(User).filter(User.login == login).one_or_none()
    return user


@dataclass
class UserData:
    login: str
    password: str
    user_type: UserTypeEnum


def create_user(
        db_session: Session,
        user_data: UserData) -> User:
    existing_user = get_user_by_login(db_session, user_data.login)
    if existing_user is not None:
        raise UserAlreadyExistsException
    user = User(
        login=user_data.login,
        hashed_password=get_password_hash(user_data.password),
        type=user_data.user_type,
    )
    db_session.add(user)
    db_session.flush()
    db_session.refresh(user)
    return user


def create_user_full(
        db_session: Session,
        user_data: UserData,
        profile_data: ProfileDataType) -> User:
    with db_session.begin():
        user_type = user_data.user_type
        user = create_user(db_session, user_data)
        _ = create_profile(db_session, user.id, user_type, profile_data)
    return user
