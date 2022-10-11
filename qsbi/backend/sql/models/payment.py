# coding: utf-8
from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base


class Payment(Base):  # type: ignore
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    account_id = Column(Integer, ForeignKey("account.id"))
    current = Column(Integer)  # if not None, automatic numbering
    type_id = Column(Integer, ForeignKey("paymenttype.id"))

    account = relationship("Account", back_populates="payments")
    type = relationship("PaymentType", back_populates="payments")
