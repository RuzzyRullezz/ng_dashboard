from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool

from neopay_api import config

pool_engine = create_engine(
    config.DB_DSN,
    poolclass=QueuePool,
)
SessionPool = sessionmaker(autocommit=False, autoflush=False, expire_on_commit=True, bind=pool_engine)
