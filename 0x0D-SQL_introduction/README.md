## :pencil2:  SQL - Introduction

This folder contains some scripts to use the open source database management software MySQL. Here we found commands to create and delete MySQL databases, how to access a database, how to create a table, how to add information to a table, how to update information in the table among others.

### Requirements:
All commands were tested on Ubuntu 14.04 LTS. Although the commands might work fine on other distributions, versions or operative systems.

Additionally, MySQL database management software was used. The version of MySQL: 14.14 Distrib 5.5.62, for debian-linux-gnu (x86_64) using readline 6.3.

If you don't have MySQL installed, download it and install as shown (Ubuntu):

    sudo apt-get install mysql-server

### Usage:
You need to execute as follows:

    cat file.sql | mysql -hlocalhost -uroot -p

Some of the files additionally require that you pass the name of the database with which you want to work or that you want to modify. In these cases the execution will be like this:

    cat file.sql | mysql -hlocalhost -uroot -p mydatabase

### Executable files:

Here a short description of each script:

+ [0-list_databases.sql](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/0-list_databases.sql): A script that lists all databases of your MySQL server.
+ [1-create_database_if_missing.sql](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/1-create_database_if_missing.sql): A script that creates the database hbtn_0c_0 in your MySQL server. If the database hbtn_0c_0 already exists, don't fail.
+ [2-remove_database.sql](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/2-remove_database.sql): A script that deletes the database hbtn_0c_0 in your MySQL server. If the database hbtn_0c_0 doesn’t exist, don't fail.
+ [3-list_tables.sql](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/3-list_tables.sql): A script that lists all the tables of a database in your MySQL server. The database name will be passed as argument of mysql command.
+ [4-first_table.sql](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/4-first_table.sql): A script that creates a table called first_table in the current database in your MySQL server. first_table description: id INT, name VARCHAR(256).
+ [5-full_table.sql](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/5-full_table.sql): Script that prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server.
+ [6-list_values.sql](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/6-list_values.sql): Script that lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server.
+ [7-insert_value.sql](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/7-insert_value.sql): Script that inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server.
+ [8-count_89.sql](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/8-count_89.sql): cript that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server.
+ [9-full_creation.sql](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/9-full_creation.sql): Script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows. second_table description:
id INT, name VARCHAR(256), score INT. Create these records: id = 1, name = “John”, score = 10; id = 2, name = “Alex”, score = 3; id = 3, name = “Bob”, score = 14; id = 4, name = “George”, score = 8.
+ [10-top_score.sql](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/10-top_score.sql): Script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server. Results should display both the score and the name (in this order). Records should be ordered by score (top first).
+ [11-best_score.sql](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/11-best_score.sql): Script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server. Results should display both the score and the name (in this order). Records should be ordered by score (top first).
+ [12-no_cheating.sql](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/12-no_cheating.sql): Script that updates the score of Bob to 10 in the table second_table.
+ [13-change_class.sql](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/13-change_class.sql): Script that removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in your MySQL server.
+ [14-average.sql](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/14-average.sql): Script that computes the score average of all records in the table second_table of the database hbtn_0c_0 in your MySQL server. The result column name should be average.
+ [15-groups.sql](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/15-groups.sql): Script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server. The result should display: the score and the number of records for this score with the label number. The list should be sorted by the number of records (descending).
+ [16-no_link.sql](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/16-no_link.sql): Script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server. Don’t list rows without a name value. Results should display the score and the name (in this order). Records should be listed by descending score.
+ [101-avg_temperatures.sql](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/101-avg_temperatures.sql): Script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
+ [102-top_city.sql](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/102-top_city.sql): Script that displays the top 3 of cities temperature during July and August ordered by temperature (descending).
+ [103-max_state.sql](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/103-max_state.sql): Script that displays the max temperature of each state (ordered by State name).
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE5MTMwMDk3ODFdfQ==
-->
