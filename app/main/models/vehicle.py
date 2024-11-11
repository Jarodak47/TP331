from dataclasses import dataclass
from enum import Enum
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Text, Table, Boolean,types,event,Float
from datetime import datetime
from sqlalchemy.orm import relationship
from .db.base_class import Base
from .base import TimestampMixin

@dataclass
class Vehicle(TimestampMixin,Base):
    __tablename__ = 'vehicles'

    uuid: str = Column(String, primary_key=True, index=True)
    brand: str = Column(String, nullable=False, index=True)
    model: str = Column(String, nullable=False, index=True)
    
    year: int = Column(Integer, nullable=False, index=True)
    color: str = Column(String, nullable=False, index=True)
    quantity: int = Column(Integer, nullable=False, index=True)

    is_rentable: bool = Column(Boolean, nullable=False, default=False)
    is_purchasable: bool = Column(Boolean, nullable=False, default=False)
    is_bookable: bool = Column(Boolean, nullable=False, default=False)

    ads = relationship('AdVehicle', back_populates='vehicle')
    # reservations = relationship('Reservation', back_populates='vehicle')
    payments = relationship('Payment', back_populates='vehicle')

    def __repr__(self):
        return f'<Vehicle: brand: {self.brand}, model: {self.model}, year: {self.year}, color: {self.color}, is_rentable: {self.is_rentable}, is_purchasable: {self.is_purchasable}>'
