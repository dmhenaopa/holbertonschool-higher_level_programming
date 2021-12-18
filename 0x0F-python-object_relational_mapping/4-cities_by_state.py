#!/usr/bin/python3
"""
   Module with script that list all cities from database hbtn_0e_4_usa
"""
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
        def select_by_name(self, table_name_1, table_name_2):
            """
               Select the elements where name matches the argument

               Args:
                   name: argument with name of state to select
            """
            sql = "SELECT table1.id, table1.name, table2.name \
                    FROM {} AS table1 JOIN {} AS table2 \
                    ON table1.state_id = table2.id \
                    ORDER BY id ASC".format(table_name_1, table_name_2)

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
    database.select_by_name('cities', 'states')
    database.close()
