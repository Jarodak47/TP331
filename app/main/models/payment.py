from dataclasses import dataclass
from sqlalchemy import Column, ForeignKey, String,types,Float
from sqlalchemy.orm import relationship

from .user import EnumList
from .db.base_class import Base
from .base import TimestampMixin

@dataclass
class Payment(TimestampMixin,Base):
    __tablename__ = 'payments'

    user_uuid: str = Column(String, ForeignKey('users.uuid'), primary_key=True)
    vehicle_uuid: str = Column(String, ForeignKey('vehicles.uuid'), primary_key=True)

    user = relationship('User', back_populates='payments')
    vehicle = relationship('Vehicle', back_populates='payments')

    total_paid: float = Column(Float, nullable=False)
    total_due: float = Column(Float, nullable=False)
    type: str = Column(types.Enum(EnumList), index=True, nullable=False, default=EnumList.NONE)
