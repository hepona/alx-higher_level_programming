#!/usr/bin/python3
"""takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa"""
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
        "SELECT cities.name FROM cities, states\
         WHERE states.id = cities.state_id AND\
         states.name = %s ORDER BY cities.id ",
        (argv[4], )
    )
    results = cursor.fetchall()
    for idx, i in enumerate(results):
        print("{}".format(i[0]), end=", " if idx < len(results) - 1 else '')
    print()
    cursor.close()
    db.close()
