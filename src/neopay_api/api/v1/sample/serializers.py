from pydantic import BaseModel


class SampleRequest(BaseModel):
    code: str
    value: int


class SampleResponse(BaseModel):
    msg: str
