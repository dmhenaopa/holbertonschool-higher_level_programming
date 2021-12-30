#!/usr/bin/python3
"""
   Module that contains the class definition of a States
   and an instance Base = declarative_base()
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """Definition of class State that inherits from Base class"""
    __tablename__ = 'states'

    id = Column(Integer(), unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state')
