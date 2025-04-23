from sqlalchemy import Column, Integer, String, Float, Enum, DateTime, Date, ForeignKey, CheckConstraint, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base import Base


class AmortSchedule(Base):
    __tablename__ = "amort_schedule"

    record_id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    loan_id = Column(Integer, ForeignKey("loans.loan_id"), nullable=False)
    amount = Column(Float, nullable=False)
    collection_date = Column(Date, nullable=False)
    is_paid = Column(Boolean, default=False)

    loan = relationship("Loan", back_populates="amort_schedule")
 