from typing import Any

from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    id: Any
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    @classmethod
    def discover(cls):
        from neopay_api.core.logging.incoming_request_log import models as incoming_request_log_models
        from neopay_api.core.users import models as users_models
