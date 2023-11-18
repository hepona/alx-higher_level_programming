#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db_host = "localhost"
    db_user = argv[1]
    db_passwd = argv[2]
    db = argv[3]
    port = 3306
    db = MySQLdb.connect(
            host=db_host,
            port=port,
            user=db_user,
            passwd=db_passwd,
            db=db
    )
    cursor = db.cursor()
    cursor.execute(
        "SELECT c.id, c.name, s.name FROM cities c`\
        JOIN states s ON s.id = c.state_id ORDER BY id "
    )
    r = cursor.fetchall()
    print(r)
    for row in r:
        print("{}".format(row))
    cursor.close()
    db.close()
