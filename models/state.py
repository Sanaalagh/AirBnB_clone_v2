#!/usr/bin/python3
"""Defines the State class."""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """Represents a state for a MySQL database.

    Inherits from SQLAlchemy Base and links to the MySQL table states.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store States.
        name (sqlalchemy String): The name of the State.
        cities (sqlalchemy relationship): The State-City relationship.
    """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', cascade='all, delete', backref='state')
    else:
        @property
        def cities(self):
            """Getter attribute to return the list of City objects."""
            cities_list = []
            all_cities = models.storage.all('City')
            for city in all_cities.values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """Getter attribute to return the list of City objects."""
            from models import storage
            cities_list = []
            for city in storage.all('City').values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
