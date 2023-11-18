#!/usr/bin/python3
"""prints the first State object from the database hbtn_0e_6_usa"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, text

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        )
    )
    with engine.connect() as cn:
        r = cn.execute(text("SELECT * FROM states WHERE id = 1 ORDER BY id"))
        for row in r:
            print("{}: {}".format(row[0], row[1]))
