#!/usr/bin/python3
"""
   Module with script that changes the name of a State object
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

    session.query(State)\
           .filter(State.id == 2)\
           .update({
                    State.name: 'New Mexico'
                   })

    session.commit()
    session.close()
