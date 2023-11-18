#!/usr/bin/python3
"""the class definition of a State and an instance Base = declarative_base()"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

m = MetaData()
Base = declarative_base(metadata=m)


class State(Base):
    """State attribute"""

    __tablename__ = "States"
    id = Column(
        Integer, primary_key=True, unique=True,
        autoincrement=True, nullable=False
    )
    name = Column(String(128), nullable=False)
