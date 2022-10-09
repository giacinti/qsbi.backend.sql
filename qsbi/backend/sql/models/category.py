# coding: utf-8
from sqlalchemy import Column, Float, Integer, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from .base import Base

class Category(Base):  # type: ignore
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    type_id = Column(Integer, ForeignKey("categorytype.id"))
    
    type = relationship("CategoryType", back_populates="categories")
    
    sub_categories = relationship("SubCategory", back_populates="category")
    schedules = relationship("Scheduled", back_populates="category")
    transacts = relationship("Transact", back_populates="category")
