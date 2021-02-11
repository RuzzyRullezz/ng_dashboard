import getpass
from typing import Optional

from fastapi import Depends, HTTPException
from jose import jwt, JWTError
from neopay_api import config
from neopay_api.core.users.models import User, UserTypeEnum
from neopay_api.core.users import store as users_store
from neopay_api.core.users.profiles import store as profiles_store
from neopay_api.core.users.auth import verify_password, oauth2_scheme, TokenPayload
from neopay_api.db.session import get_db_local_session
from neopay_api.db.session_pool import SessionPool
from sqlalchemy.orm import Session
from starlette import status

user_type_input_map = {str(i + 1): user_type for i, user_type in enumerate(list(UserTypeEnum))}


def user_type_input_map_verbose() -> str:
    tokens = [f"{k} - {v}" for k, v in user_type_input_map.items()]
    if len(tokens) == 0:
        return ''
    result_str = ', '.join(tokens)
    return result_str


def cli_create_user():
    login = input("Login: ")
    password = getpass.getpass(prompt='Password: ', stream=None)
    while (user_type_input := input(f"Type ({user_type_input_map_verbose()}): ")) not in list(user_type_input_map.keys()):
        pass
    user_type = user_type_input_map[user_type_input]
    profile_data_dict = dict(
        first_name=input("First name: "),
        last_name=input("Last name: "),
        country=input("Country: "),
        phone=input("Phone: "),
    )
    if user_type == UserTypeEnum.client:
        # TODO: просим ввести поля для заказчика
        ...
    elif user_type == UserTypeEnum.executor:
        # TODO: просим ввести поля для исполнителя
        ...
    else:
        raise NotImplementedError(f"Unsupported user_type {user_type}")
    profile_data_cls = profiles_store.get_profile_data_cls(user_type)
    profile_data = profile_data_cls(**profile_data_dict)
    db_session = SessionPool()
    try:
        users_store.create_user(db_session, login, password, user_type, profile_data)
    finally:
        db_session.close()


def get_user_by_login_and_password(db_session: Session, login: str, password: str) -> Optional[User]:
    user = users_store.get_user_by_login(db_session, login)
    if user is None:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user


def user_from_request(
        token: str = Depends(oauth2_scheme),
        db_session: Session = Depends(get_db_local_session)) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload: TokenPayload = TokenPayload.parse_obj(
            jwt.decode(token, config.SECRET_KEY, algorithms=[config.ALGORITHM])
        )
    except JWTError:
        raise credentials_exception
    user = users_store.get_user_by_login(db_session, payload.login)
    if user is None:
        raise credentials_exception
    return user
