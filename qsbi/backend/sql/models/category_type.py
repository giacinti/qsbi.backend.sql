# coding: utf-8
from sqlalchemy import Column, Float, Integer, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from .base import Base

class CategoryType(Base):
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    
    categories = relationship("Category", back_populates="type")