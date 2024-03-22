#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship

# Association table for the many-to-many relationship
place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey(
                          'places.id'), primary_key=True, nullable=False),
                      Column('amenity_id', String(60), ForeignKey(
                          'amenities.id'), primary_key=True, nullable=False)
                      )


class Place(BaseModel, Base):
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship("Review", backref="place", cascade="all, delete")
    amenities = relationship(
            "Amenity", secondary=place_amenity, viewonly=False,
            back_populates="place_amenities")

    # For FileStorage
    @property
    def amenities(self):
        """Returns the list of Amenity instances."""
        return self.amenity_ids

    @amenities.setter
    def amenities(self, obj):
        """Adds an Amenity.id to the amenity_ids."""
        if type(obj).__name__ == 'Amenity':
            self.amenity_ids.append(obj.id)

    @property
    def reviews(self):
        """Returns the list of Review instances
        with place_id equals to the current Place.id"""
        from models import storage
        all_reviews = storage.all(Review).values()
        return [review for review in all_reviews if review.place_id == self.id]
