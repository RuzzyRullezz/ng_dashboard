import datetime

from pydantic import BaseModel

from neopay_api.core.users.models import UserTypeEnum


class Token(BaseModel):
    access_token: str
    token_type: str


class UserInfoResponse(BaseModel):
    login: str
    type: UserTypeEnum
    created_at: datetime.datetime
