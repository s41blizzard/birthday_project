import sqlite3
import smtplib

conn = sqlite3.connect('employees.sqlite')

cursor = conn.cursor()

cursor.execute(
    "SELECT id, LastName, FirstName from employees WHERE strftime('%m',DOB) = strftime('%m','now') AND  strftime('%d','now') = strftime('%d', DOB)")

results = cursor.fetchall()

print(results)
conn.close()
smtpObj = smtplib.SMTP('smtp.yandex.com', 587)
smtpObj.starttls()
smtpObj.login('s41blizzard@yandex.ru', 'Gravity84')
smtpObj.sendmail("s41blizzard@yandex.ru", "s41.blizzard@mail.ru", "test test")

# текущая день месяц strftime('%m','now'), strftime('%d','now')
# запрос для др "SELECT id, LastName, FirstName from employees WHERE strftime('%m',DOB) = strftime('%m','now') AND  strftime('%d','now') = strftime('%d', DOB)"
###
