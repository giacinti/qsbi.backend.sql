# coding: utf-8
from sqlalchemy import Column, Float, Integer, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from .base import Base

class User(Base):
    id = Column(Integer, primary_key=True)
    login = Column(Text)
    firstname = Column(Text)
    lastname = Column(Text)
    notes = Column(Text)

    logs = relationship("AuditLog", back_populates="user")
