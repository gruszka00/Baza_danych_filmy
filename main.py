import mysql.connector

mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  password='gerard_gruszka',
  port='3306',
  database='Films'
)

query= 'SELECT title, year from Films'

cursor = mydb.cursor()
cursor.execute(query)

for films in cursor:
  print(films)

