# coding: utf-8
from sqlalchemy import Column, Float, Integer, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from .base import Base

class PaymentType(Base):
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    
    payments = relationship("Payment", back_populates="type")
