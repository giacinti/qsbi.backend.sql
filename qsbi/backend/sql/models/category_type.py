# coding: utf-8
from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import relationship

from .base import Base


class CategoryType(Base):  # type: ignore
    id = Column(Integer, primary_key=True)
    name = Column(Text)

    categories = relationship("Category", back_populates="type")
