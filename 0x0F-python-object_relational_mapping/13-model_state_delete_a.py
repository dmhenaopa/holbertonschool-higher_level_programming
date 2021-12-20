#!/usr/bin/python3
"""
   Module with script that deletes all State objects
   that contain the letter a from the database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
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

    states = session.query(State).filter(State.name.contains("a"))

    for state in states:
        session.delete(state)

    session.commit()
    session.close()
