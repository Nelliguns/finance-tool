from sqlalchemy import Column, Boolean, ForeignKey, Integer, String, Float
from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String, nullable=False)



class HoldingItem(Base):
    __tablename__ = "holdingitems"

    id = Column(Integer, primary_key=True)
    company = Column(String, unique=True)
    holding = Column(Float)

