#!/usr/bin/python3
"""
Start link class to table in database
"""
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    sessionmaker_ = sessionmaker(bind=engine)
    session = sessionmaker_()
    instance = session.query(State).order_by(State.id).all()
    for ins in instance:
        print("{}: {}".format(ins.id, ins.name), end="")
        for city in ins.cities:
            print("    ", end="")
            print("{}: {}".format(city.id, city.name), end="")
