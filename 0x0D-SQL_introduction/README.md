Tasks
0. List databases
mandatory

Write a script that lists all databases of your MySQL server.



Repo:

    GitHub repository: alx-higher_level_programming
    Directory: 0x0D-SQL_introduction
    File: 0-list_databases.sql

1. Create a database
mandatory

Write a script that creates the database hbtn_0c_0 in your MySQL server.

    If the database hbtn_0c_0 already exists, your script should not fail
    You are not allowed to use the SELECT or SHOW statements



Repo:

    GitHub repository: alx-higher_level_programming
    Directory: 0x0D-SQL_introduction
    File: 1-create_database_if_missing.sql

2. Delete a database
mandatory

Write a script that deletes the database hbtn_0c_0 in your MySQL server.

    If the database hbtn_0c_0 doesn’t exist, your script should not fail
    You are not allowed to use the SELECT or SHOW statements



Repo:

    GitHub repository: alx-higher_level_programming
    Directory: 0x0D-SQL_introduction
    File: 2-remove_database.sql

3. List tables
mandatory

Write a script that lists all the tables of a database in your MySQL server.

    The database name will be passed as argument of mysql command (in the following example: mysql is the name of the database)



Repo:

    GitHub repository: alx-higher_level_programming
    Directory: 0x0D-SQL_introduction
    File: 3-list_tables.sql

4. First table
mandatory

Write a script that creates a table called first_table in the current database in your MySQL server.

    first_table description:
        id INT
        name VARCHAR(256)
    The database name will be passed as an argument of the mysql command
    If the table first_table already exists, your script should not fail
    You are not allowed to use the SELECT or SHOW statements


Repo:

    GitHub repository: alx-higher_level_programming
    Directory: 0x0D-SQL_introduction
    File: 4-first_table.sql

5. Full description
mandatory

Write a script that prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server.

    The database name will be passed as an argument of the mysql command
    You are not allowed to use the DESCRIBE or EXPLAIN statements



Repo:

    GitHub repository: alx-higher_level_programming
    Directory: 0x0D-SQL_introduction
    File: 5-full_table.sql

6. List all in table
mandatory

Write a script that lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server.

    All fields should be printed
    The database name will be passed as an argument of the mysql command


Repo:

    GitHub repository: alx-higher_level_programming
    Directory: 0x0D-SQL_introduction
    File: 6-list_values.sql

7. First add
mandatory

Write a script that inserts a new row in the table first_table (database hbtn_0c_0) in your MySQL server.

    New row:
        id = 89
        name = Best School
    The database name will be passed as an argument of the mysql command


Repo:

    GitHub repository: alx-higher_level_programming
    Directory: 0x0D-SQL_introduction
    File: 7-insert_value.sql

8. Count 89
mandatory

Write a script that displays the number of records with id = 89 in the table first_table of the database hbtn_0c_0 in your MySQL server.

    The database name will be passed as an argument of the mysql command


Repo:

    GitHub repository: alx-higher_level_programming
    Directory: 0x0D-SQL_introduction
    File: 8-count_89.sql

9. Full creation
mandatory

Write a script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.

    second_table description:
        id INT
        name VARCHAR(256)
        score INT
    The database name will be passed as an argument to the mysql command
    If the table second_table already exists, your script should not fail
    You are not allowed to use the SELECT and SHOW statements
    Your script should create these records:
        id = 1, name = “John”, score = 10
        id = 2, name = “Alex”, score = 3
        id = 3, name = “Bob”, score = 14
        id = 4, name = “George”, score = 8


Repo:

    GitHub repository: alx-higher_level_programming
    Directory: 0x0D-SQL_introduction
    File: 9-full_creation.sql

10. List by best
mandatory

Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.

    Results should display both the score and the name (in this order)
    Records should be ordered by score (top first)
    The database name will be passed as an argument of the mysql command



Repo:

    GitHub repository: alx-higher_level_programming
    Directory: 0x0D-SQL_introduction
    File: 10-top_score.sql

11. Select the best
mandatory

Write a script that lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0 in your MySQL server.

    Results should display both the score and the name (in this order)
    Records should be ordered by score (top first)
    The database name will be passed as an argument of the mysql command



Repo:

    GitHub repository: alx-higher_level_programming
    Directory: 0x0D-SQL_introduction
    File: 11-best_score.sql

12. Cheating is bad
mandatory

Write a script that updates the score of Bob to 10 in the table second_table.

    You are not allowed to use Bob’s id value, only the name field
    The database name will be passed as an argument of the mysql command



Repo:

    GitHub repository: alx-higher_level_programming
    Directory: 0x0D-SQL_introduction
    File: 12-no_cheating.sql

13. Score too low
mandatory

Write a script that removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in your MySQL server.

    The database name will be passed as an argument of the mysql command



Repo:

    GitHub repository: alx-higher_level_programming
    Directory: 0x0D-SQL_introduction
    File: 13-change_class.sql

14. Average
mandatory

Write a script that computes the score average of all records in the table second_table of the database hbtn_0c_0 in your MySQL server.

    The result column name should be average
    The database name will be passed as an argument of the mysql command


Repo:

    GitHub repository: alx-higher_level_programming
    Directory: 0x0D-SQL_introduction
    File: 14-average.sql

15. Number by score
mandatory

Write a script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server.

    The result should display:
        the score
        the number of records for this score with the label number
    The list should be sorted by the number of records (descending)
    The database name will be passed as an argument to the mysql command

 

Repo:

    GitHub repository: alx-higher_level_programming
    Directory: 0x0D-SQL_introduction
    File: 15-groups.sql

16. Say my name
mandatory

Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.

    Don’t list rows without a name value
    Results should display the score and the name (in this order)
    Records should be listed by descending score
    The database name will be passed as an argument to the mysql command

In this example, new data have been added to the table second_table.



Repo:

    GitHub repository: alx-higher_level_programming
    Directory: 0x0D-SQL_introduction
    File: 16-no_link.sql

17. Go to UTF8
#advanced

Write a script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.

You need to convert all of the following to UTF8:

    Database hbtn_0c_0
    Table first_table
    Field name in first_table



Repo:

    GitHub repository: alx-higher_level_programming
    Directory: 0x0D-SQL_introduction
    File: 100-move_to_utf8.sql

18. Temperatures #0
#advanced

Import in hbtn_0c_0 database this table dump: download

Write a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).


Repo:

    GitHub repository: alx-higher_level_programming
    Directory: 0x0D-SQL_introduction
    File: 101-avg_temperatures.sql

19. Temperatures #1
#advanced

Import in hbtn_0c_0 database this table dump: download (same as Temperatures #0)

Write a script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)


Repo:

    GitHub repository: alx-higher_level_programming
    Directory: 0x0D-SQL_introduction
    File: 102-top_city.sql

20. Temperatures #2
#advanced

Import in hbtn_0c_0 database this table dump: download (same as Temperatures #0)

Write a script that displays the max temperature of each state (ordered by State name).



Repo:

    GitHub repository: alx-higher_level_programming
    Directory: 0x0D-SQL_introduction
    File: 103-max_state.sql
