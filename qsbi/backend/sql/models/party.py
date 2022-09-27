# coding: utf-8
from sqlalchemy import Column, Float, Integer, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from .base import Base

class Party(Base):
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    desc = Column(Text)

    schedules = relationship("Scheduled", back_populates="party")
    transacts = relationship("Transact", back_populates="party")
