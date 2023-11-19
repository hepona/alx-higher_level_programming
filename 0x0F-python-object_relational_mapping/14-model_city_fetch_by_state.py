#!/usr/bin/python3
"""prints all City objects from the database hbtn_0e_14_usa"""
from sys import argv
from sqlalchemy import create_engine, update
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from model_city import Base, City

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}"
        .format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True,
    )
    Session = sessionmaker()
    session = Session(bind=engine)
    Base.metadata.create_all(engine)
    r = session.query(City, State).order_by(City.id)
    for i in r:
        print("{}: ({}) {}".format(i.State.name, i.City.id, i.City.name))
