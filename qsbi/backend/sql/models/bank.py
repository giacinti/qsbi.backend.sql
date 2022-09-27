# coding: utf-8
from sqlalchemy import Column, Float, Integer, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from .base import Base

class Bank(Base):
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    code = Column(Integer)
    bic = Column(Text)
    address = Column(Text)
    tel = Column(Text)
    mail = Column(Text)
    web = Column(Text)
    contact_name = Column(Text)
    contact_fax = Column(Text)
    contact_tel = Column(Text)
    contact_mail = Column(Text)
    notes = Column(Text)
    
    accounts = relationship("Account", back_populates="bank")
