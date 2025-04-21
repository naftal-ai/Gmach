from sqlalchemy import Column, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from app.db.base import Base


class Guarantor(Base):
    __tablename__ = "guarantors"

    req_id = Column(Integer, ForeignKey("loan_req.req_id"), nullable=False)
    customers = Column(Integer, ForeignKey("customers.customer_id"), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)

    loan_req = relationship("LoanReq", back_populates="borrowers")
    customers = relationship("Customer", back_populates="borrowers")