import sqlite3


def _sqlite_connect_and_query():
    conn = sqlite3.connect('employees.sqlite')
    cursor = conn.cursor()

    results = cursor.fetchall()

    conn.close()
