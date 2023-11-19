#!/usr/bin/python3
"""delete all State objects with a name containing the letter a
 from the database hbtn_0e_6_usa"""
from sys import argv
from sqlalchemy import create_engine, update
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}"
        .format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True,
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(State).filter(State.name.like("%a%"))\
        .delete()
    session.commit()
    session.close()
