# coding: utf-8
from sqlalchemy import Column, Float, Integer, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from .base import Base

class SubCategory(Base):
    id = Column(Integer, primary_key=True)
    category_id = Column(Integer, ForeignKey("category.id"), primary_key=True)
    name = Column(Text)
    
    category = relationship("Category", back_populates="sub_categories")
    schedules = relationship("Scheduled", back_populates="sub_category")
    transacts = relationship("Transact", back_populates="sub_category")
