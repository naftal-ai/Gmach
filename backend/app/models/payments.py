from sqlalchemy import Column, Integer, String, Float, Enum, DateTime, ForeignKey, CheckConstraint, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base
import enum

frequency_valid = CheckConstraint("frequency BETWEEN 1 AND 12", name="frequency_valid")
collection_day_valid = CheckConstraint("frequency IN (1, 10, 15)", name="collction_day_valid")


class PaymentType(enum.Enum):
    REGULAR_COLLECTION = "regular_collection"
    ARREARS = "arrers"
    PREPAYMENT = "prepayment"
    LOAN_ORIGINATION_FEE = "loan_origination_fee"

class PaymentMethod(enum.Enum):
    CASH = "cash"
    CHECK = "check"
    DIRECT_DEBIT = "direct_debit"
    BANK_TRASFER = "bank_trasfer"


class PaymentStatus(enum.Enum):
    PENDING = "pending"
    REJECTED = "rejected"
    APPROVED = "approved"
 


class Payment(Base):
    __tablename__ = "payments"

    payment_id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    payment_type = Column(Enum(PaymentType), default=PaymentType.REGULAR_COLLECTION, nullable=False)
    payment_method = Column(Enum(PaymentMethod), nullable=False)
    payment_date = Column(DateTime, server_default=func.now(), nullable=False)
    amount = Column(Float, nullable=False)
    payment_status = Column(Enum(PaymentStatus), default=PaymentStatus.PENDING, nullable=False)
    req_id = Column(Integer, ForeignKey("loan_req.req_id"), nullable=True)
    loan_id = Column(Integer, ForeignKey("loans.loan_id"), nullable=True)
    schedule_id = Column(Integer, ForeignKey("amort_schedule.record_id"), nullable=True)
    payer_id = Column(String(10), nullable=False)
    payer_name = Column(String(40), nullable=False)
    approval_at = Column(DateTime, nullable=True)
    rejected_at = Column(DateTime, nullable=True)
    bank = Column(String(3), nullable=True)
    branch = Column(String(4), nullable=True)
    account = Column(String(15), nullable=True)

    #relationships
    loan_req = relationship("LoanReq", back_populates="payments")
    loan = relationship("Loan", back_populates="payments")
    schedule = relationship("AmortSchedule", back_populates="payments")