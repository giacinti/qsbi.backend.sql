from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from qsbi.backend.sql.config import settings

engine = create_engine(
    settings.QSBI_DB_URL,
    # required for sqlite
    connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
