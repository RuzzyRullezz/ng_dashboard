from .base import ApiError

ForbiddenOperation = ApiError(code="forbidden_operation", detail="Operation is forbidden for account.")
UnAuthorized = ApiError(code="unauthorized", detail="Unauthorized.")
MethodNotImplemented = ApiError(code="method_not_implemented", detail="Method is not implemented.")
