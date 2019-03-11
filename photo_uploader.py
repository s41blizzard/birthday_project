import sqlite3
import os

# пока не готово
conn = sqlite3.connect('employees.sqlite')
cursor = conn.cursor()
cursor.execute('SELECT id,  FIO from zup_employees')
results = cursor.fetchall()
print(results)
file_list = os.listdir(r'C:\Users\s41bl\PycharmProjects\project_birthday\empl_photo')

file_names = [os.path.splitext(x)[0] for x in file_list]
file_names_trimmed = []
for i in file_names:
    file_names_trimmed.append(i.strip())

print(file_names_trimmed)
