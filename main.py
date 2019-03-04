import sqlite3
import smtplib
import schedule
import time


def checking_birthdays():
    conn = sqlite3.connect('employees.sqlite')
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, LastName, FirstName from employees WHERE strftime('%m',DOB) = strftime('%m','now') AND  strftime('%d','now') = strftime('%d', DOB)")

    results = cursor.fetchall()

    # print(results[0][1])
    conn.close()
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.starttls()
    smtpObj.login('zard.41@gmail.com', 'gravity84')
    for empl in results:
        subject = "День рождения сотрудника"
        body = "Поздавляем сотрудника " + empl[1] + " " + empl[2] + " с Днем Рождения!"
        message = 'Subject: {}\n\n{}'.format(subject, body)
        # text = "Поздавляем сотрудника " + empl[1] + " " + empl[2] + " с Днем Рождения!"
        text_encoded = message.encode('utf-8').strip()
        smtpObj.sendmail("zard.41@gmail.com", "s41.blizzard@mail.ru", text_encoded)


schedule.every().day.at("07:00").do(checking_birthdays)
while True:
    schedule.run_pending()
    time.sleep(60)
# текущая день месяц strftime('%m','now'), strftime('%d','now')
# запрос для др "SELECT id, LastName, FirstName from employees WHERE strftime('%m',DOB) = strftime('%m','now') AND  strftime('%d','now') = strftime('%d', DOB)"
###
