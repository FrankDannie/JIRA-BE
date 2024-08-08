from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database URL for SQLite; use a different URL for production (e.g., PostgreSQL)
SQLALCHEMY_DATABASE_URL = "sqlite:///./JIRA.db"

# Create the SQLAlchemy engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}  # Necessary for SQLite to allow multiple threads
)

# Create a configured "Session" class
SessionLocal = sessionmaker(
    autocommit=False,  # Disable autocommit to manage transactions manually
    autoflush=False,  # Disable autoflush to control when changes are flushed to the database
    bind=engine,  # Bind the session to the database engine
)

# Base class for declarative models
Base = declarative_base()
