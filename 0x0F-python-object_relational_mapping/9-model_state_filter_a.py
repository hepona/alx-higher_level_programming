#!/usr/bin/python3
"""lists all State objects that contain the letter
a from the database hbtn_0e_6_usa"""
import sys
import MySQLdb
from model_state import Base, State
from sqlalchemy import create_engine, select, text
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        )
    )
    Session = sessionmaker()
    session = Session(bind=engine)
    Base.metadata.create_all(engine)
    r = session.query(State).order_by(State.id).\
        filter(State.name.like("%a%")).all()
    for i in r:
        print("{}: {}".format(i.id, i.name))
    session.close()
