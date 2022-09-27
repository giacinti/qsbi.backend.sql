# coding: utf-8
from sqlalchemy import Column, Float, Integer, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship, backref

from .base import Base

class Transact(Base):
    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey("account.id"))
    transaction_date = Column(DateTime)
    value_date = Column(DateTime)
    party_id = Column(Integer, ForeignKey("party.id"))
    category_id = Column(Integer, ForeignKey("category.id"))
    sub_category_id = Column(Integer, ForeignKey("subcategory.id"))
    notes = Column(Text)
    amount = Column(Float)
    currency_id = Column(Integer, ForeignKey("currency.id"))
    exchange_rate = Column(Float)
    exchange_fees = Column(Float)
    payment_id = Column(Integer, ForeignKey("payment.id"))
    master_id = Column(Integer, ForeignKey("transact.id"))
    reconcile_id = Column(Integer, ForeignKey("reconcile.id"))
    log_id = Column(Integer, ForeignKey("auditlog.id"))

    account = relationship("Account", back_populates="transacts")
    party = relationship("Party", back_populates="transacts")
    category = relationship("Category", back_populates="transacts")
    sub_category = relationship("SubCategory", back_populates="transacts")
    currency = relationship("Currency")
    payment = relationship("Payment")
#    master = relationship("Transact")
    reconcile = relationship("Reconcile")
    log = relationship("AuditLog", back_populates="transacts")

    subs = relationship("Transact", backref=backref('master', remote_side=[id]))
    

