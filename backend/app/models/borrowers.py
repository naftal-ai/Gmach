from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base import Base


class Borrower(Base):
    __tablename__ = "borrowers"

    req_id = Column(Integer, ForeignKey("loan_req.req_id", ondelete="CASCADE"), nullable=False)
    borrower_id = Column(Integer, ForeignKey("customers.customer_id"), nullable=False)

    loan_req = relationship("LoanReq", back_populates="borrowers")
    customers = relationship("Customer", back_populates="borrowers")