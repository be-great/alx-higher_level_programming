#!/usr/bin/python3
"""
Start link class to table in database
"""
import sys
from relationship_city import City
from relationship_state import State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    sessionmaker_ = sessionmaker(bind=engine)
    session = sessionmaker_()
    instance_state = State(name="California")
    instance_city = City(name="San Francisco")
    instance_state.cities.append(instance_city)
    session.add(instance_state)
    session.add(instance_city)
    session.commit()
    session.close()
