#!/usr/bin/python3
"""module for conect to database"""

import MySQLdb
import sys
import re

if __name__ == "__main__":
    """generate main"""
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    var = "SELECT cities.name FROM states\
        INNER JOIN cities ON states.id = cities.state_id\
        WHERE states.name LIKE '%{}%'\
        ORDER BY cities.id ASC".format(sys.argv[4])
    cur.execute(var)
    query_rows = cur.fetchall()
    coma = 0
    for row in query_rows:
        cad = re.sub(",|\\(|\\)|\'", "", str(row))
        print(cad, end='')
        coma += 1
        if coma < len(query_rows):
            print(", ", end="")
    print()
    cur.close()
    conn.close()
