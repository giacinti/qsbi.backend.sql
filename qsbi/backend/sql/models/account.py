# coding: utf-8
from sqlalchemy import Column, Float, Integer, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from .base import Base


class Account(Base):  # type: ignore
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    bank_id = Column(Integer, ForeignKey("bank.id"))
    bank_branch = Column(Text)
    bank_account = Column(Text)
    bank_account_key = Column(Text)
    bank_IBAN = Column(Text)
    currency_id = Column(Integer, ForeignKey("currency.id"))
    open_date = Column(DateTime)
    close_date = Column(DateTime)
    type_id = Column(Integer, ForeignKey("accounttype.id"))
    initial_balance = Column(Float)
    mini_balance_wanted = Column(Float)
    mini_balance_auth = Column(Float)
    holder_name = Column(Text)
    holder_address = Column(Text)
    notes = Column(Text)

    bank = relationship("Bank", back_populates="accounts")
    currency = relationship("Currency", back_populates="accounts")
    type = relationship("AccountType", back_populates="accounts")

    reconciles = relationship("Reconcile", back_populates="account")
    schedules = relationship("Scheduled", back_populates="account")
    transacts = relationship("Transact", back_populates="account")
    payments = relationship("Payment", back_populates="account")
