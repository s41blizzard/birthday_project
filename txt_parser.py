import sqlite3

conn = sqlite3.connect('employees.sqlite')
cursor = conn.cursor()
cursor.execute("SELECT id from zup_employees")
ids = cursor.fetchall()
ids_list = []
for item in ids:
    ids_list.append(item[0])
print(ids_list)
with open(r'C:\Users\s41bl\PycharmProjects\project_birthday\for_empl_list\zup_employees.txt',
          encoding="utf-8-sig") as x:
    for line in x:
        line_arr = (line.split('\t'))
        empl_id = line_arr[0]
        if empl_id not in ids_list:
            firstName = line_arr[1]
            print(firstName)
            lastName = line_arr[2]
            dob = line_arr[3]
            ok_dob = list(reversed(dob.split('.')))
            date_ready = '-'.join(ok_dob)
            gender = line_arr[4]
            hiring_date = line_arr[5]
            ok_hiring_date = list(reversed(hiring_date.split('.')))
            hiring_date_ready = '-'.join(ok_hiring_date)
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO zup_employees (id, FirstName, LastName, DOB, GENDER, HIRING_DATE) VALUES (?, ?, ?,?, ?, ?)",
                (empl_id, firstName, lastName, date_ready, gender, hiring_date_ready))
            conn.commit()

conn.close()
