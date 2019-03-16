import sqlite3
import os

conn = sqlite3.connect('employees.sqlite')
cursor = conn.cursor()
cursor.execute('SELECT id,  LastName, FirstName from zup_employees WHERE PHOTO IS NULL')
results = cursor.fetchall()

presumedFileNameList = []
for el in results:
    presumedFileNameList.append(el[1] + ' ' + el[2])

photo_list = os.listdir(r'C:\Users\s41bl\PycharmProjects\project_birthday\empl_photo')
photo_path = r'C:\Users\s41bl\PycharmProjects\project_birthday\empl_photo'
file_names = [os.path.splitext(x)[0] for x in photo_list]
file_names_trimmed = []
for i in file_names:
    file_names_trimmed.append(i.strip())
for photo in file_names_trimmed:

    if photo in presumedFileNameList:
        photo_bytes = open(photo_path + '\\' + photo + '.jpg', 'rb').read()
        cursor = conn.cursor()
        cursor.execute("UPDATE zup_employees SET PHOTO = ? WHERE FirstName = ? AND LastName = ?",
                       (photo_bytes, photo.split(" ")[1], photo.split(" ")[0]))
        conn.commit()

conn.close()
