#!/usr/bin/python3
# displays all cities of a state from database
# safe from SQL injection
# Usage: ./5-filter_cities.py <mysql username> \
#                             <mysql password> \
#                             <database name> \
#                             <state_name_to_search>
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `cities` as `c` \
               INNER JOIN `states` as `s` \
               ON `c`.`state_id` = `s`.`id` \
               ORDER BY `c`.`id`")
    print(", ".join([ct[2] for ct in c.fetchall() if ct[4] == sys.argv[4]]))
