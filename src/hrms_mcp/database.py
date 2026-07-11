from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.hrms_mcp.config import DATABASE_URL
engine=create_engine(
    DATABASE_URL,
    echo=False
)

SessionLocal=sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)