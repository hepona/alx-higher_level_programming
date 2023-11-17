#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""
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
        db=db,
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ")
    result = cursor.fetchall()
    for row in result:
        print("({}, '{}')".format(row[0], row[1]))
    cursor.close()
    db.close()
