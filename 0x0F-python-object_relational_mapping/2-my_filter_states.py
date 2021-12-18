#!/usr/bin/python3
"""
   Module with script that list all values in states
   table where name matches
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    hostname = "localhost"
    number_port = 3306
    username = argv[1]
    password = argv[2]
    database_name = argv[3]
    state_name = argv[4]

    class DataBase:
        """Parent class DataBase with connection to SQL database"""
        def __init__(self):
            """Constructor method to initialize the DataBase instance"""
            self.connection = MySQLdb.connect(
                host=hostname,
                port=number_port,
                user=username,
                passwd=password,
                db=database_name
            )

            self.cursor = self.connection.cursor()

        """----------------------------Methods--------------------------"""
        def select_by_name(self, state_name):
            """
               Select the elements where name matches the argument

               Args:
                   name: argument with name of state to select
            """
            sql = "SELECT * FROM states WHERE name = '{}' \
                ORDER BY id ASC".format(state_name)

            try:
                self.cursor.execute(sql)
                rows = self.cursor.fetchall()

                for row in rows:
                    print(row)

            except Exception as e:
                raise

        def close(self):
            """
               Close the connection with the SQL database
            """
            self.cursor.close()
            self.connection.close()

    database = DataBase()
    database.select_by_name(state_name)
    database.close()
