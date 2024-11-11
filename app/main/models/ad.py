from dataclasses import dataclass
from enum import Enum
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Text, Table, Boolean,types,event,Float
from datetime import datetime
from sqlalchemy.orm import relationship
from .db.base_class import Base
from .base import TimestampMixin

@dataclass
class Ad(TimestampMixin,Base):
    __tablename__ = 'ads'

    uuid: str = Column(String, primary_key=True, unique=True)
    title: str = Column(String, nullable=False)
    description: str = Column(String, nullable=True)
    
    vehicles = relationship('AdVehicle', back_populates='ad')
    photos = relationship('AdPhoto', back_populates='ad')
    notification = relationship('Notification', back_populates='ad', uselist=False)
    ad_reviews = relationship('AdReview', back_populates='ad')

@dataclass
class AdVehicle(TimestampMixin,Base):
    __tablename__ = 'ad_vehicles'

    ad_uuid: str = Column(String, ForeignKey('ads.uuid'), primary_key=True)
    vehicle_uuid: str = Column(String, ForeignKey('vehicles.uuid'), primary_key=True)

    ad = relationship('Ad', back_populates='vehicles')
    vehicle = relationship('Vehicle', back_populates='ads')

@dataclass
class AdPhoto(TimestampMixin,Base):
    __tablename__ = 'ad_photos'

    ad_uuid: str = Column(String, ForeignKey('ads.uuid'), primary_key=True)
    photo_uuid: str = Column(String, ForeignKey('storages.uuid'), primary_key=True)

    ad = relationship('Ad', back_populates='photos')
    photo = relationship('Storage')

@dataclass
class AdReview(TimestampMixin,Base):
    __tablename__ = 'ad_reviews'

    user_uuid: str = Column(String, ForeignKey('users.uuid'), primary_key=True)
    ad_uuid: str = Column(String, ForeignKey('ads.uuid'), primary_key=True)
    rating: float = Column(Float, nullable=False)
    comment: str = Column(Text, nullable=True)
   
    user = relationship('User', back_populates='ad_reviews')
    ad = relationship('Ad', back_populates='ad_reviews')
