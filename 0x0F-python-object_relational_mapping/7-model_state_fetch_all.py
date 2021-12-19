#!/usr/bin/python3
"""
   Module with script that lists all State objects
   from the database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    number_port = 3306
    username = argv[1]
    password = argv[2]
    database_name = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username,
                                   password,
                                   database_name))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    """SELECT * FROM states ORDER BY id ASC;"""
    for state in session.query(State).order_by(asc(State.id)):
        print("{}: {}".format(state.id, state.name))

    session.close()
