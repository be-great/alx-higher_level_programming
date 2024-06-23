#!/usr/bin/python3
"""script that lists all states from the database"""
import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    sql = ("SELECT"
           " cities.name as city_name"
           " FROM cities"
           " INNER JOIN states on states.id=cities.state_id "
           " where states.name = %s"
           " ORDER BY cities.id ASC")
    cur.execute(sql, (sys.argv[4],))
    query_rows = cur.fetchall()
    for i in range(len(query_rows)):
        print(query_rows[i][0], end="")
        if i < len(query_rows) - 1:
            print(", ", end="")
        else:
            print()
    cur.close()
    conn.close()
