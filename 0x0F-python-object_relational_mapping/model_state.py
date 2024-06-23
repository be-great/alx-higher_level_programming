#!/usr/bin/python3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, MetaData
"""python file that contains the class """
""""definition of a State and an instance Base"""
mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """The state class"""
    __tablename__ = "states"
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
