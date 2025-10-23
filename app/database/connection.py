"""
Database connection and session management
"""

from sqlalchemy.orm import Session
from .base import SessionLocal


def get_db():
    """
    Dependency to get database session
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
