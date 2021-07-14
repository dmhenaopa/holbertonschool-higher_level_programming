## :pencil2:  SQL - More queries

This folder contains some scripts to use the open source database management software MySQL. Here we found commands to create a new user, grant privileges, create tables with some characteristics as NOT NULL, DEFAULT value, UNIQUE, PRIMARY KEY and FOREIGN KEY,  AUTO_INCREMENT. Additionaly, the use of the keywords JOIN, INNER JOIN, RIGHT JOIN and LEFT JOIN.

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

+ [0-privileges.sql](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x0E-SQL_more_queries/0-privileges.sql): Script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).
+ [1-create_user.sql](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x0E-SQL_more_queries/1-create_user.sql): Script that creates the MySQL server user user_0d_1. user_0d_1 should have all privileges on your MySQL server. The user_0d_1 password should be set to user_0d_1_pwd. If the user user_0d_1 already exists, your script should not fail.
+ [2-create_read_user.sql](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x0E-SQL_more_queries/2-create_read_user.sql): Script that creates the database hbtn_0d_2 and the user user_0d_2. user_0d_2 should have only SELECT privilege in the database hbtn_0d_2. The user_0d_2 password should be set to user_0d_2_pwd. If the database hbtn_0d_2 already exists, your script should not fail. If the user user_0d_2 already exists, your script should not fail.
+ 3-force_name.sql: Script that creates the table force_name on your MySQL server. force_name description: id INT, name VARCHAR(256) can’t be null. The database name will be passed as an argument of the mysql command. If the table force_name already exists, your script should not fail.
+ 4-never_empty.sql: Script that creates the table id_not_null on your MySQL server. id_not_null description: id INT with the default value 1, name VARCHAR(256). The database name will be passed as an argument of the mysql command. If the table id_not_null already exists, your script should not fail.
+ 5-unique_id.sql: Script that creates the table unique_id on your MySQL server. unique_id description: id INT with the default value 1 and must be unique, name VARCHAR(256).The database name will be passed as an argument of the mysql command. If the table unique_id already exists, your script should not fail.
+ 6-states.sql: Script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server. states description: id INT unique, auto generated, can’t be null and is a primary key, name VARCHAR(256) can’t be null. If the database hbtn_0d_usa already exists, your script should not fail. If the table states already exists, your script should not fail.
+ 7-cities.sql: Script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server. cities description: id INT unique, auto generated, can’t be null and is a primary key, state_id INT, can’t be null and must be a FOREIGN KEY that references to id of the states table, name VARCHAR(256) can’t be null. If the database hbtn_0d_usa already exists, your script should not fail. If the table cities already exists, your script should not fail.
+ 8-cities_of_california_subquery.sql: Script that lists all the cities of California that can be found in the database hbtn_0d_usa. The states table contains only one record where name = California. Results must be sorted in ascending order by cities.id. The database name will be passed as an argument of the mysql command.
+ 9-cities_by_state_join.sql: Script that lists all cities contained in the database hbtn_0d_usa. Each record should display: cities.id - cities.name - states.name. Results must be sorted in ascending order by cities.id. The database name will be passed as an argument of the mysql command.
+ 10-genre_id_by_show.sql: Script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked. Each record should display: tv_shows.title - tv_show_genres.genre_id. Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id. The database name will be passed as an argument of the mysql command.
+ 11-genre_id_all_shows.sql: Script that lists all shows contained in the database hbtn_0d_tvshows. Each record should display: tv_shows.title - tv_show_genres.genre_id. Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id. If a show doesn’t have a genre, display NULL. The database name will be passed as an argument of the mysql command.
+ 12-no_genre.sql: Script that lists all shows contained in hbtn_0d_tvshows without a genre linked. Each record should display: tv_shows.title - tv_show_genres.genre_id. Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id. The database name will be passed as an argument of the mysql command.
+ 13-count_shows_by_genre.sql: Script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each. Each record should display: <TV Show genre> - <Number of shows linked to this genre>. First column must be called genre. Second column must be called number_of_shows. Don’t display a genre that doesn’t have any shows linked. Results must be sorted in descending order by the number of shows linked. The database name will be passed as an argument of the mysql command.
+ 14-my_genres.sql: Script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter. The tv_shows table contains only one record where title = Dexter (but the id can be different). Each record should display: tv_genres.name. Results must be sorted in ascending order by the genre name. The database name will be passed as an argument of the mysql command.
+ 15-comedy_only.sql: Script that lists all Comedy shows in the database hbtn_0d_tvshows. The tv_genres table contains only one record where name = Comedy (but the id can be different). Each record should display: tv_shows.title. Results must be sorted in ascending order by the show title. The database name will be passed as an argument of the mysql command.
+ 16-shows_by_genre.sql: Script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows. If a show doesn’t have a genre, display NULL in the genre column. Each record should display: tv_shows.title - tv_genres.name. Results must be sorted in ascending order by the show title and genre name. The database name will be passed as an argument of the mysql command.
<!--stackedit_data:
eyJoaXN0b3J5IjpbOTU0Njg4OTI1XX0=
-->