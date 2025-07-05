from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy import Column, Integer, String, inspect
from sqlalchemy.orm import relationship
from .base import Base

class Device(Base):
    __tablename__ = "devices"

    id = Column(String, primary_key=True, nullable=False)
    device_name = Column(String(100), nullable=False)

    # Relación con DeviceGroup
    data_entries = relationship("DeviceGroup", back_populates="device")