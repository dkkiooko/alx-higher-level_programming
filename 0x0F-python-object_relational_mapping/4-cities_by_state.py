#!/usr/bin/python3
# list all cities in database, order by id
# Usage: ./4-cities_by_state.py <mysql username> \
#                               <mysql password> \
#                               <database name>
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT c.id, c.name, s.name \
               FROM cities c INNER JOIN states s \
               ON c.state_id = s.id \
               ORDER BY c.id")
    [print(city) for city in c.fetchall()]
