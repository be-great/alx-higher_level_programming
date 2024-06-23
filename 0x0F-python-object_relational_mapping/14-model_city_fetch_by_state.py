#!/usr/bin/python3
"""
Start link class to table in database
"""
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_city import City
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    sessionmaker_ = sessionmaker(bind=engine)
    session = sessionmaker_()
    cmd1 = session.query(State.name, City.id, City.name)
    citys = cmd1.filter(City.state_id == State.id).order_by(City.id).all()
    for city in citys:
        print(city)
        #print("{}: ({}) {}".format(citys[0], citys[1], citys[2]))
