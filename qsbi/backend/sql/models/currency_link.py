# coding: utf-8
from sqlalchemy import Column, Float, Integer, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from .base import Base


class CurrencyLink(Base):
    id = Column(Integer, primary_key=True)
    cur1_id = Column(Integer, ForeignKey("currency.id"))
    cur2_id = Column(Integer, ForeignKey("currency.id"))
    rate = Column(Float)
    date = Column(DateTime)
    log_id = Column(Integer, ForeignKey("auditlog.id"))
    
    cur1 = relationship("Currency", foreign_keys=[cur1_id], back_populates="exchanges")
    cur2 = relationship("Currency", foreign_keys=[cur2_id], back_populates="exchanges")
    log = relationship("AuditLog", back_populates="currency_links")
