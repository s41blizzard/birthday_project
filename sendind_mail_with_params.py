import sys
import os
import datetime
from email.message import EmailMessage
from email.utils import make_msgid
import smtplib
from PIL import Image
from io import BytesIO
import io
import os, random


def finding_employee_photo():
    fio = sys.argv[1]
    photo_list = os.listdir(r'C:\Users\s41bl\PycharmProjects\project_birthday\empl_photo')
    photo_path = r'C:\Users\s41bl\PycharmProjects\project_birthday\empl_photo\\'
    file_names = [os.path.splitext(x)[0] for x in photo_list]
    photo_bytes = ''
    now = datetime.datetime.now()
    found = False
    for el in file_names:
        if el.strip() == fio:
            f_ind = file_names.index(el)
            found = True
            photo_bytes = open(photo_path + file_names[f_ind] + '.jpg', 'rb').read()
    if not found:
        with open('logs.txt', 'a') as f:
            f.write(now.strftime("%d-%m-%Y %H:%M") + ' Фото сотрудника ' + fio + ' не найдено ' + '\n')
    return photo_bytes


def picture_overlay(photo):
    buf = BytesIO(photo)
    foreground = Image.open(buf)
    foreground_photo = foreground.resize((200, 260))
    foreground_photo = foreground_photo.convert('RGBA')
    foreground_photo = foreground_photo.rotate(5, expand=True)
    background_path = r"background\\"
    background_filename = random.choice(os.listdir(background_path))
    background = Image.open(background_path + background_filename)
    background = background.convert('RGBA')

    bwidth, bheight = background.size[0], background.size[1]
    fwidth, fheight = foreground.size[0], foreground.size[1]
    x, y = int((bwidth / 2) - (fwidth / 2)), int((bheight / 2) - (fheight / 2))  # центрирование

    background.paste(foreground_photo, (250, 250), mask=foreground_photo)
    img_bytes = io.BytesIO()
    background.save(img_bytes, format='PNG')
    img_bytes = img_bytes.getvalue()

    return img_bytes


def send_gratz(picture):
    msg = EmailMessage()
    msg['Subject'] = "Поздавляем  сотрудника " + sys.argv[1] + " с Днем Рождения!"
    msg['From'] = ("zard.41@gmail.com")
    msg['To'] = ('s41.blizzard@mail.ru, zard.41@gmail.com')
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
    msg.get_payload()[1].add_related(picture, 'pic.jpg', 'jpeg',
                                     cid=asparagus_cid)
    # Send the message via local SMTP server.
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.starttls()
    smtpObj.login('zard.41@gmail.com', 'bi31V3Iu4J')
    with smtpObj as s:
        s.send_message(msg)


empl_photo = finding_employee_photo()
gratz_card = picture_overlay(empl_photo)
send_gratz(gratz_card)
