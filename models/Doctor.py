from sqlalchemy import Column, Integer, ForeignKey, Text, Boolean
from sqlalchemy.orm import relationship

from BaseModel import BaseModel


class Doctor(BaseModel):
    __tablename__ = 'doctors'

    person_id = Column(Integer, ForeignKey('person_info.id'))
    position = Column(Text)
    is_active = Column(Boolean, default=True)

    person_info = relationship('PersonInfo', lazy='join',
                               foreign_keys=[person_id])
