#!/usr/bin/python3
"""Module with script that list all states from database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    hostname = "localhost"
    number_port = 3306
    username = argv[1]
    password = argv[2]
    database_name = argv[3]

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
        def select_all(self, table_name):
            """
               Select all the elements in table

               Args:
                   table_name: String with name of table
            """
            sql = 'SELECT * FROM {} ORDER BY id ASC'.format(table_name)

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
database.select_all('states')
database.close()
