#!/usr/bin/python3
"""script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument."""
import sys
import MySQLdb
import sys

if __name__ == "__main__":
    db_host = "localhost"
    db_user = sys.argv[1]
    db_passwd = sys.argv[2]
    db = sys.argv[3]
    port = 3306
    db = MySQLdb.connect(
        host=db_host,
        port=port,
        user=db_user,
        passwd=db_passwd,
        db=db
    )
    cursor = db.cursor()
    arg = sys.argv[4]
    q = "SELECT * FROM states WHERE name = '" + arg + "' ORDER BY id"
    cursor.execute(q)
    r = cursor.fetchall()
    for row in r:
        print("({}, '{}')".format(row[0], row[1]))
    cursor.close()
    db.close()
