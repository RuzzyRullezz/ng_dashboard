from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from neopay_api.core.users import manager
from neopay_api.core.users.auth import create_access_token
from neopay_api.core.users.models import User
from neopay_api.db.session import get_db_local_session, SessionLocal
from sqlalchemy.orm import Session
from starlette import status

from .serializers import UserInfoResponse, Token
from . import errors


router = APIRouter()


@router.post(
    "/login/",
    tags=["Users"],
    response_model=Token,
    operation_id="login",
)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db_session: Session = Depends(get_db_local_session)):
    user = manager.get_user_by_login_and_password(db_session, form_data.username, form_data.password)
    if user is None:
        raise errors.IncorrectCredentials.as_api_exception(status.HTTP_400_BAD_REQUEST)
    access_token = create_access_token(user.login)
    return Token(
        access_token=access_token,
        token_type="bearer"
    )


@router.get(
    "/info/",
    response_model=UserInfoResponse,
    tags=["Users"],
    operation_id="user-info",
)
def user_info(user: User = Depends(manager.user_from_request)):
    return UserInfoResponse(
        login=user.login,
        created_at=user.created_at,
    )