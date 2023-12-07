from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, func
from datetime import datetime

from core.database import Base, engine


class TodoModel(Base):
    __tablename__ = "todo"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    description = Column(String(500))
    complete = Column(Boolean, default=False)
    updated_at = Column(DateTime, nullable=True, default=None, onupdate=datetime.now)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    owner_id = Column(Integer, ForeignKey("users.id"))
