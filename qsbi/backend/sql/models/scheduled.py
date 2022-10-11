# coding: utf-8
from sqlalchemy import Column, Float, Integer, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship, backref

from .base import Base


class Scheduled(Base):  # type: ignore
    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey("account.id"))
    start_date = Column(DateTime)
    limit_date = Column(DateTime)
    frequency = Column(Integer)
    automatic = Column(Integer)
    party_id = Column(Integer, ForeignKey("party.id"))
    category_id = Column(Integer, ForeignKey("category.id"))
    sub_category_id = Column(Integer, ForeignKey("subcategory.id"))
    notes = Column(Text)
    amount = Column(Float)
    currency_id = Column(Integer, ForeignKey("currency.id"))
    payment_id = Column(Integer, ForeignKey("payment.id"))
    splitted = Column(Integer)
    master_id = Column(Integer, ForeignKey("scheduled.id"))
    log_id = Column(Integer, ForeignKey("auditlog.id"))

    account = relationship("Account", back_populates="schedules")
    party = relationship("Party", back_populates="schedules")
    category = relationship("Category", back_populates="schedules")
    sub_category = relationship("SubCategory", back_populates="schedules")
    currency = relationship("Currency")
    payment = relationship("Payment")
#    master = relationship("Scheduled")
    log = relationship("AuditLog", back_populates="schedules")

    subs = relationship("Scheduled", backref=backref('master', remote_side=[id]))
