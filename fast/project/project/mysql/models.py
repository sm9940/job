from sqlalchemy import Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import mapped_column, relationship
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = mapped_column(String(255), nullable=False)
    email = mapped_column(String(255), unique=True, nullable=False)
    histories = relationship("History", back_populates="owner", cascade="all, delete")
    is_active = mapped_column(Boolean,default=False)

class History(Base):
    __tablename__ = "histories"
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    title = mapped_column(String(255), nullable=False)
    description = mapped_column(String(255))
    owner_id = mapped_column(Integer, ForeignKey("users.id"))
    owner = relationship("User",back_populates="histories")
