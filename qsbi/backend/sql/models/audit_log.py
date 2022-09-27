# coding: utf-8
from sqlalchemy import Column, Float, Integer, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from .base import Base

class AuditLog(Base):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    date = Column(DateTime)
    notes = Column(Text)

    user = relationship("User", back_populates="logs")
    
    reconciles = relationship("Reconcile", back_populates="log")
    currency_links = relationship("CurrencyLink", back_populates="log")
    transacts = relationship("Transact", back_populates="log")
    schedules = relationship("Scheduled", back_populates="log")
