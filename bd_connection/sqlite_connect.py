import sqlite3


def _sqlite_connect_and_query():
    conn = sqlite3.connect('employees.sqlite')
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, LastName, FirstName, Photo from employees WHERE strftime('%m',DOB) = strftime('%m','now') AND  strftime('%d','now') = strftime('%d', DOB)")

    results = cursor.fetchall()

    conn.close()
