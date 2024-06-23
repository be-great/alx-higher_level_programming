#!/usr/bin/python3
"""
Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    sessionmaker_ = sessionmaker(bind=engine)
    session = sessionmaker_()
    cmd1 = session.query(State).filter(State.name == sys.argv[4])
    states = cmd1.first()
    if states is None:
        print("Not found")
    else:
        print("{}".format(states.id))
