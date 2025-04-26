from sqlalchemy import Column, Integer, String, Float, Enum, DateTime, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base
from models.loan_req import collection_day_valid, frequency_valid
import enum


class Loan(Base):
    __tablename__ = "loans"

    loan_id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    req_id = Column(Integer, ForeignKey("loan_req.req_id"), nullable=False)
    amount = Column(Float, nullable=False)
    payments_no = Column(Integer, default=12)
    frequency = Column(Integer, frequency_valid, nullable=False, default=1)
    created_at = Column(DateTime, server_default=func.now())
    is_active = Column(Boolean, default=True)
    bank = Column(String(3), nullable=True)
    branch = Column(String(4), nullable=True)
    account = Column(String(15), nullable=True)
    collection_day = Column(Integer, collection_day_valid)
    start_payment_date = Column(Date, nullable=False)

    loan_req = relationship("LoanReq", back_populates="loans")
    amort_schedule = relationship("AmortSchedule", back_populates="loan")
    payments = relationship("Payment", back_populates="loans")