# coding: utf-8
from sqlalchemy import Column, Float, Integer, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from .base import Base


class Currency(Base):
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    nickname = Column(Text)
    code = Column(Text)
    
    accounts = relationship("Account", back_populates="currency")
    exchanges = relationship("CurrencyLink", primaryjoin="or_(CurrencyLink.cur1_id==Currency.id,"
                             "CurrencyLink.cur2_id==Currency.id)")
