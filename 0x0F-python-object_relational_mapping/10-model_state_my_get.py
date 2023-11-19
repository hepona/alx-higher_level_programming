#!/usr/bin/python3
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

"""prints the State object with the name passed as
argument from the database hbtn_0e_6_usa"""

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    s = session.query(State).order_by(State.id).all()
    found = 0
    for state in s:
        if state.name == sys.argv[4]:
            print("{}".format(state.id))
            found = 1
    if found == 0:
        print("Not found")
    session.close()
