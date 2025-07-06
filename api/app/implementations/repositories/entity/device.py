from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy import Column, Integer, String, inspect
from sqlalchemy.orm import relationship
from .base import Base

class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, autoincrement=True)
    device_id = Column(String(100), nullable=False, unique=True)
    device_name = Column(String(100), nullable=False)

    # Relación con DeviceGroup
    data_entries = relationship("DeviceGroup", back_populates="device")