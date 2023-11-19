#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

"""prints the State object with the name passed as
argument from the database hbtn_0e_6_usa"""

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = (
        session.query(State).where(State.name == sys.argv[4]).order_by(State.id).first()
    )
    if not state:
        print("Not found")
    else:
        print("{}".format(state.id))
    session.close()
