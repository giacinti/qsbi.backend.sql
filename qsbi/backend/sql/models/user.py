# coding: utf-8
import json
from typing import List
from sqlalchemy import Column, Float, Integer, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from .base import Base

class User(Base):  # type: ignore
    id = Column(Integer, primary_key=True)
    login = Column(Text)
    firstname = Column(Text)
    lastname = Column(Text)
    password = Column(Text)
    active = Column(Integer)
    scopes_str = Column(Text)
    notes = Column(Text)

    @property
    def scopes(self) -> List:
        lst: List = []
        if self.scopes_str:
            lst = json.loads(str(self.scopes_str))
        return lst

    @scopes.setter
    def scopes(self, lst) -> None:
        self.scopes_str = json.dumps(lst)

    logs = relationship("AuditLog", back_populates="user")
