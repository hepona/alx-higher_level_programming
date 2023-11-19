#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

"""prints the State object with the name passed as
argument from the database hbtn_0e_6_usa"""

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ), pool_pre_pint=True
    )
    Session = sessionmaker()
    session = Session(bind=engine)
    nm = sys.argv[4]
    state = session.query(State).filter(State.name == nm).\
        order_by(State.id).all()
    if not state:
        print("Not found")
    for s in state:
        print("{}".format(s.id))
    session.close()
