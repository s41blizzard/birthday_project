import sqlite3

conn = sqlite3.connect('employees.sqlite')

cursor = conn.cursor()

cursor.execute(
    "SELECT id, LastName, FirstName from employees WHERE strftime('%m',DOB) = strftime('%m','now') AND  strftime('%d','now') = strftime('%d', DOB)")

results = cursor.fetchall()

print(results)
conn.close()

# текущая день месяц strftime('%m','now'), strftime('%d','now')
# запрос для др "SELECT id, LastName, FirstName from employees WHERE strftime('%m',DOB) = strftime('%m','now') AND  strftime('%d','now') = strftime('%d', DOB)"
###
