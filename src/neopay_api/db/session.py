from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from neopay_api import config


engine = create_engine(
    config.DB_DSN,
    pool_pre_ping=True,
)
# Используется только в веб-запросах или быстрых скриптах
SessionLocal = sessionmaker(autocommit=False, autoflush=False, expire_on_commit=True, bind=engine)


def get_db_local_session() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

