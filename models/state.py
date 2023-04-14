#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, Sequence, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
import models
from models.city import City


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"

    name = Column(String(128), nullable=False)

    cities = relationship("City",  backref="state")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """"returns the list of City instances"""
            listofcities = []
            allcititesinstance = models.storage.all(City)
            for i in allcititesinstance.values():
                if i.state_id == self.id:
                    listofcities.append(i)
            return listofcities
