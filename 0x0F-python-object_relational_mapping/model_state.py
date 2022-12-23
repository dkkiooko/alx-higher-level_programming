#!/usr/bin/python3
""" defines a State model
# inherits from SQLalchemy Base and links to the MySQL table states
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base


class State(Base):
    """represents state for MySQL database

    Args:
        Base (_sqlalchemy_): _factory function which all entities inherit_
    """
    __tablename__ = "states"
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
