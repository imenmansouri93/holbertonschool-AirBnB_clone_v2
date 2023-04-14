#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from models.state import State
from sqlalchemy import Column, Integer, Sequence, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    if storage_t == 'db':
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey(State.id), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place")
    else:
        state_id = ""
        name = """"
