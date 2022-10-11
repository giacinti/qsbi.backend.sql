# coding: utf-8
from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import relationship

from .base import Base


class Party(Base):  # type: ignore
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    desc = Column(Text)

    schedules = relationship("Scheduled", back_populates="party")
    transacts = relationship("Transact", back_populates="party")
