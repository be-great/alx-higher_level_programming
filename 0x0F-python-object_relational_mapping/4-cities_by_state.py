#!/usr/bin/python3
"""script that lists all states from the database"""
#!/usr/bin/python3
"""script that lists all states from the database"""

import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host = "localhost", port = 3306, user = sys.argv[1],
                            passwd = sys.argv[2], db = sys.argv[3], charset="utf8")
    cur = conn.cursor()
    sql = "SELECT id, states.name as state_name, name FROM cities inner join states on state_id = states.id ORDER BY id ASC"
    cur.execute(sql)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
