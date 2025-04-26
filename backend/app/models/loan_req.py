from sqlalchemy import Column, Integer, String, Float, Enum, DateTime, CheckConstraint, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base
import enum

frequency_valid = CheckConstraint("frequency BETWEEN 1 AND 12", name="frequency_valid")
collection_day_valid = CheckConstraint("frequency IN (1, 10, 15)", name="collction_day_valid")

class ReqStatus(enum.Enum):
    PENDING = "pending"
    REJECTED = "rejected"
    APPROVED = "approved"
    COMPLITED = "complited"


class LoanReq(Base):
    __tablename__ = "loan_req"

    req_id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    payments_no = Column(Integer, default=12)
    frequency = Column(Integer, frequency_valid, nullable=False, default=1)
    purpose = Column(String(255))
    opened_at = Column(DateTime, server_default=func.now())
    req_status = Column(Enum(ReqStatus), default=ReqStatus.PENDING)
    is_signed = Column(Boolean, default=False)
    approval_at = Column(DateTime, nullable=True)
    rejected_at = Column(DateTime, nullable=True)
    signed_at = Column(DateTime, nullable=True)
    payment_bank = Column(String(3), nullable=True)
    payment_branch = Column(String(4), nullable=True)
    payment_account = Column(String(15), nullable=True)
    collection_bank = Column(String(3), nullable=True)
    collection_branch = Column(String(4), nullable=True)
    collection_account = Column(String(15), nullable=True)
    collection_day = Column(Integer, collection_day_valid)

    borrowers = relationship("Borrower", back_populates="loan_req")
    guarantors = relationship("Guarantor", back_populates="loan_req")
    loans = relationship("Loan", back_populates="loan_req")
    payments = relationship("Payment", back_populates="loan_req")
