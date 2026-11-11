from sqlalchemy import Column, Integer, String
from src.database import Base


class Customer(Base):
    __tablename__ = "customers_practice"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False, index=True)