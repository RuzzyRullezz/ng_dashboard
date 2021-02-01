import datetime
import functools
import pathlib

from sqlalchemy.engine.url import URL, make_url
from starlette.config import Config
from starlette.datastructures import Secret

from . import loggers


config_path = pathlib.Path(__file__).parent.absolute() / ".env"
config = Config(str(config_path))


ALLOWED_ORIGINS = [
    "*",
]

TESTING = config("TESTING", cast=bool, default=False)

DB_DRIVER = config("DB_DRIVER", default="postgresql")
DB_HOST = config("DB_HOST", default='127.0.0.1')
DB_PORT = config("DB_PORT", cast=int, default=5432)
DB_USER = config("DB_USER", default='neopay_api')
DB_PASSWORD = config("DB_PASSWORD", cast=Secret, default='neopay_api')
DB_DATABASE = config("DB_DATABASE", default='neopay_api')
DB_DSN = config(
    "DB_DSN",
    cast=make_url,
    default=URL(
        drivername=DB_DRIVER,
        username=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
        database=DB_DATABASE,
    ),
)
DB_POOL_MIN_SIZE = config("DB_POOL_MIN_SIZE", cast=int, default=1)
DB_POOL_MAX_SIZE = config("DB_POOL_MAX_SIZE", cast=int, default=16)
DB_ECHO = config("DB_ECHO", cast=bool, default=False)
DB_SSL = config("DB_SSL", default=None)
DB_USE_CONNECTION_FOR_REQUEST = config(
    "DB_USE_CONNECTION_FOR_REQUEST", cast=bool, default=True
)
DB_RETRY_LIMIT = config("DB_RETRY_LIMIT", cast=int, default=1)
DB_RETRY_INTERVAL = config("DB_RETRY_INTERVAL", cast=int, default=1)

# Logging
TG_TOKEN = config("TG_TOKEN", cast=str, default=None)
TG_CHAT = config("TG_CHAT", cast=int, default=None)
SENTRY_DSN = config("SENTRY_DSN", cast=str, default=None)
setup_logging = functools.partial(loggers.setup, tg_token=TG_TOKEN, tg_chat=TG_CHAT, sentry_dsn=SENTRY_DSN)

# Auth
SECRET_KEY = config("SECRET_KEY", cast=str, default="060e751fcdd6a203ef39e2563ebe60fec39fed9d4043081e3a15a8278be972f8")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_INTERVAL = datetime.timedelta(days=365)
