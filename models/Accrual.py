from sqlalchemy import Column, Integer, ForeignKey, DateTime, DECIMAL
from sqlalchemy.orm import relationship

from BaseModel import BaseModel


class Accrual(BaseModel):
    __tablename__ = 'accruals'

    patient_id = Column(Integer, ForeignKey('patients.id'))
    date = Column(DateTime, nullable=False)
    sum = Column(DECIMAL, default=0)

    patient = relationship('Patient', lazy='join',
                           foreign_keys=[patient_id])