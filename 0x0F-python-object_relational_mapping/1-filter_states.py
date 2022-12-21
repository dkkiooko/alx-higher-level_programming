#!/usr/bin/python3
# list all states with a name starting with N from database
# usage: ./1-filter_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states` WHERE name LIKE BINARY 'N%' \
               ORDER BY `id`")
    [print(state) for state in c.fetchall()]
