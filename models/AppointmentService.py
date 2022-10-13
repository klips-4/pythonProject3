from sqlalchemy import Column, Integer, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship

from BaseModel import BaseModel


class AppointmentService(BaseModel):
    __tablename__ = 'appointment_services'

    patient_id = Column(Integer, ForeignKey('patients.id'))
    doctor_id = Column(Integer, ForeignKey('doctors.id'))
    service_id = Column(Integer, ForeignKey('services.id'))
    count = Column(Integer, nullable=False)
    date_complete = Column(DateTime)
    date_appointment = Column(DateTime, nullable=False)

    patient = relationship('Patient', lazy='join',
                           foreign_keys=[patient_id])
    doctor = relationship('Doctor', lazy='join',
                          foreign_keys=[doctor_id])
    service = relationship('Service', lazy='join',
                           foreign_keys=[service_id])
