#!/usr/bin/python3
"""
   Module with script that prints all City objects
   from the database hbtn_0e_14_usa
"""
from sys import argv
from model_state import Base, State
from model_city import City
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    number_port = 3306
    username = argv[1]
    password = argv[2]
    database_name = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, database_name),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
