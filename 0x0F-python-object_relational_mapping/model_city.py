#!/usr/bin/python3
"""
   Module that contains the class definition of a City
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State

Base = declarative_base()


class City(Base):
    """Definition of class City that inherits from Base class"""
    __tablename__ = 'cities'

    id = Column(Integer(), unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer(), nullable=False, ForeignKey('states.id'))
