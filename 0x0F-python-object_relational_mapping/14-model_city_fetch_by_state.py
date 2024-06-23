#!/usr/bin/python3
"""
Start link class to table in database
"""
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    sessionmaker_ = sessionmaker(bind=engine)
    session = sessionmaker_()
    cmd1 = session.query(City)
    citys = cmd1.order_by(City.id).all()
    for i in range(len(citys)):
        state = session.query(State).filter(State.id == citys.state_id)
        state = state.first()
        print("{}: {} {}".format(state.name, citys[i].id, citys[i].name))
    session.commit()
