#!/usr/bin/python3
"""
   Module with script that prints the first State object
   from the database hbtn_0e_6_usa
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

    """SELECT * FROM states ORDER BY id ASC;"""
    state = session.query(State).filter(State.id == 1)

    if state is None:
        print("Nothing")

    else:
        print("{}: {}".format(state.id, state.name))

    session.close()
