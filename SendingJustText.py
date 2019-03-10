import sqlite3
import smtplib


conn = sqlite3.connect('employees.sqlite')
cursor = conn.cursor()
cursor.execute(
    "SELECT id, LastName, FirstName, Photo from employees WHERE strftime('%m',DOB) = strftime('%m','now') AND  strftime('%d','now') = strftime('%d', DOB)")

results = cursor.fetchall()

conn.close()
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.starttls()
smtpObj.login('zard.41@gmail.com', 'gravity84')
for empl in results:
    print(empl)
    subject = "День рождения сотрудника"
    body = "Поздавляем сотрудника " + empl[1] + " " + empl[2] + " с Днем Рождения!"
    message = 'Subject: {}\n\n{}'.format(subject, body)

    text_encoded = message.encode('utf-8').strip()
    # smtpObj.sendmail("zard.41@gmail.com", "s41.blizzard@mail.ru", text_encoded)

