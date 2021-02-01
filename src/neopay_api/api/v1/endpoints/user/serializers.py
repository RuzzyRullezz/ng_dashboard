import datetime

from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class UserInfoResponse(BaseModel):
    login: str
    created_at: datetime.datetime
