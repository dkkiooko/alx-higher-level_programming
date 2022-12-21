#!/usr/bin/python3
# list all values in `states` table where `name` matches
# the third argument
# Usage: ./2-my_filter_states.py <mysql username> \
#                                <mysql password> \
#                                <database name> \
#                                <state_name_to_search>

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states` WHERE BINARY `name` = '{}' \
               ORDER BY id".format(sys.argv[4]))
    [print(state) for state in c.fetchall()]
