#!/usr/bin/python3
"""
Place module
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import place_amenity

class Place(BaseModel, Base):
    """
    Place class
    """
    __tablename__ = 'places'

    city_id = Column(String(60), nullable=False, ForeignKey('cities.id'))
    user_id = Column(String(60), nullable=False, ForeignKey('users.id'))
    name = Column(String(128), nullable=False)

    amenities = relationship("Amenity", secondary="place_amenity", viewonly=False)

