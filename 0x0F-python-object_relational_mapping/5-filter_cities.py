#!/usr/bin/python3
"""script that lists all states from the database"""
import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host = "localhost", port = 3306, user = sys.argv[1],
                            passwd = sys.argv[2], db = sys.argv[3], charset="utf8")
    cur = conn.cursor()
    sql = ("SELECT" 
            " cities.name as city_name"
            " FROM cities "
            " inner join states on cities.state_id = states.id"
            " where states.name = %s"
            " ORDER BY cities.id ASC")
    cur.execute(sql, (sys.argv[4],))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row[0], end=", ")
    cur.close()
    conn.close()
