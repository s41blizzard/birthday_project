import smtplib
import sqlite3
from email.message import EmailMessage
from email.utils import make_msgid
from PictureOverlay import picture_overlay

conn = sqlite3.connect('employees.sqlite')
cursor = conn.cursor()
cursor.execute(
    "SELECT FirstName, LastName, GENDER, PHOTO from zup_employees WHERE strftime('%m',DOB) = strftime('%m','now') AND  strftime('%d','now') = strftime('%d', DOB)")

results = cursor.fetchall()
print(results)
conn.close()

# Create the base text message.
for item in results:
    pic_sql = item[3]
    overlayed_pic = picture_overlay(pic_sql, item[2])
    msg = EmailMessage()
    msg['Subject'] = "Поздавляем  сотрудника " + item[0] + " " + item[1] + " с Днем Рождения!"
    msg['From'] = ("zard.41@gmail.com")
    msg['To'] = ('s41.blizzard@mail.ru')
    msg.set_content("""\
    test test
    """)
    asparagus_cid = make_msgid()
    msg.add_alternative("""\
    <html>
      <head></head>
      <body>

        <img src="cid:{asparagus_cid}" />
      </body>
    </html>
    """.format(asparagus_cid=asparagus_cid[1:-1]), subtype='html')
    msg.get_payload()[1].add_related(overlayed_pic, 'pic.jpg', 'jpeg',
                                     cid=asparagus_cid)
    # Send the message via local SMTP server.
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.starttls()
    smtpObj.login('zard.41@gmail.com', 'bi31V3Iu4J')
    with smtpObj as s:
        s.send_message(msg)
