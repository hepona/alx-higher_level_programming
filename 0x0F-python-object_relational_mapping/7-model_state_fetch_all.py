#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_6_usa"""
import sys
from model_state import Base, State
from sqlalchemy import Column, Integer, String, MetaData, create_engine, text
from sqlalchemy.ext.declarative import declarative_base

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    with engine.connect() as connection:
        r = connection.execute(text("SELECT * FROM states ORDER BY id"))
        for i in r:
            print("{}: {}".format(i[0], i[1]))
