#!/usr/bin/python3
"""Defines the DBStorage class."""
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from os import getenv

from models.base_model import BaseModel, Base
from models.user import User


class DBStorage:
    """This class manages storage of hbnb models in a MySQL database."""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object."""
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(
                f'mysql+mysqldb://{user}:{password}@{host}/{db}',
                pool_pre_ping=True)

    def all(self, cls=None):
        """Query on the current database session
        all objects depending on the class name."""
        all_objs = {}
        if cls:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = f'{obj.__class__.__name__}.{obj.id}'
                all_objs[key] = obj
        else:
            classes = [User]  # Add other classes here
            for cls in classes:
                objs = self.__session.query(cls).all()
                for obj in objs:
                    key = f'{obj.__class__.__name__}.{obj.id}'
                    all_objs[key] = obj
        return all_objs

    def new(self, obj):
        """Add the object to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reload the database session."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
                bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close the session."""
        self.__session.close()
