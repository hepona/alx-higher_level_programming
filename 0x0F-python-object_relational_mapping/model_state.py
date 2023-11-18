#!/usr/bin/python3
"""the class definition of a State and an instance Base = declarative_base()"""
from sqlalchemy import Column, Integer, String, MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base
import sys
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
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
Base.metadata.create_all(engine)