# coding: utf-8
from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import relationship

from .base import Base

class AccountType(Base):
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    accounts = relationship("Account", back_populates="type")
