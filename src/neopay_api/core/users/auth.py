import datetime

from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from neopay_api.core.utils.datetimes import utc_now
from passlib.context import CryptContext
from pydantic.main import BaseModel

from neopay_api import config


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/user/login/")


class TokenPayload(BaseModel):
    login: str
    exp: datetime.datetime


def verify_password(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password) -> str:
    return pwd_context.hash(password)


def create_access_token(login: str):
    token_content = TokenPayload(
        login=login,
        exp=utc_now() + config.ACCESS_TOKEN_EXPIRE_INTERVAL,
    )
    encoded_jwt = jwt.encode(token_content.dict(), config.SECRET_KEY, algorithm=config.ALGORITHM)
    return encoded_jwt
