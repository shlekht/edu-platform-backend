from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from core.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    echo=True,
    pool_pre_ping=True,
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)

def get_session():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()


