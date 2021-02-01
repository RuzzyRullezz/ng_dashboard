from neopay_api.api.errors.base import ApiError

IncorrectCredentials = ApiError(code="incorrect_credentials", detail="Incorrect Credentials")
