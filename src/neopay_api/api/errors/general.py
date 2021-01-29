from .base import ApiError

ForbiddenOperation = ApiError(code=1000, detail="Operation is forbidden for account.")
UnAuthorized = ApiError(code=1001, detail="Unauthorized.")
MethodNotImplemented = ApiError(code=1002, detail="Method is not implemented.")
