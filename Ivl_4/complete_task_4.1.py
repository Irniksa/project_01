# Таблицу students добавляем в БД teachers

import sqlite3
import pandas as pd

con1 = sqlite3.connect('Students.db')
query = "SELECT * FROM Students"
df = pd.read_sql(query,con1)
print(df)

#con2 = sqlite3.connect("teachers.db")
#df.to_sql("Students", con2, index = False)
df.to_excel('students.xlsx', index = False)


# Сама задача
import sqlite3
def test(student_id):
  con = sqlite3.connect("teachers.db")
  cur = con.cursor()
  query = "SELECT * FROM School JOIN Students ON School.School_Id = Students.School_Id WHERE Students.Student_Id = ?"
  cur.execute(query, (student_id,))
  result = cur.fetchall()
  con.close()
  print ('ID студента: ',result[0][3])
  print ('Имя студента: ',result[0][4])
  print ('ID школы: ',result[0][0])
  print ('Название школы: ',result[0][1])


x = input("Введите ID студента: ")

test(x)


