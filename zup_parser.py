import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('employees.sqlite')
tree = ET.parse("Message_ЗК_FL.xml")
root = tree.getroot()
cursor = conn.cursor()
cursor.execute("SELECT id from zup_employees")
ids = cursor.fetchall()
ids_list = []
for item in ids:
    ids_list.append(item[0])
for empl in root.iter('CatalogObject.ФизическиеЛица'):
    empl_id = empl.find('Code').text
    if empl_id not in ids_list:
        fio = empl.find('ФИО').text
        dob = empl.find('ДатаРождения').text
        gender = empl.find('Пол').text
        cursor = conn.cursor()
        cursor.execute("INSERT INTO zup_employees (id, FIO, DOB, GENDER) VALUES (?, ?, ?,?)", (empl_id, fio, dob, gender))
        conn.commit()
conn.close()
