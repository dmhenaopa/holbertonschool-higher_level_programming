#!/usr/bin/python3
"""
   Module with script that list all states from database hbtn_0e_0_usa
"""
from sqlalchemy import create_engine
engine = create_engine('mysql://root:root@localhost:3306/)
 
