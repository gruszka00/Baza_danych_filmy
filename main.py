import mysql.connector

mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  password='gerard_gruszka',
  port='3306',
  database='Films'
)

cursor = mydb.cursor()
cursor.execute("USE Films")
cursor.execute("ALTER TABLE Films AUTO_INCREMENT=1")





class Film:
  def __init__(self, id, title, year):
    self.id = id
    self.title = title
    self.year = year

  def save(self):
    query = "SELECT * FROM Films WHERE id = " + str(self.id)
    cursor.execute(query)
    row = cursor.fetchone()
    if row is None:
     query = "INSERT INTO Films (title, year) SELECT " \
     "'" + self.title + "', " \
     "'" + self.year + "', "
     cursor.execute(query)
    else:
      query = "UPDATE Films SET " \
      "id = " + str(self.id) + ", " \
      "title = '" + self.title + "', " \
      "year = '" + self.year + "', " \
      " WHERE id = " + str(self.id)
      cursor.execute(query)

  @staticmethod
  def all():
    list = []
    cursor.execute("SELECT * FROM Films")
    for A in cursor:
      list.append(Film(A[0], A[1], A[2]))
    return list

def addc(list, title, year):
  list.append(Film(list[-1].id + 1, title, year))

filmy = Film.all()
addc(filmy,"Prestige","2010")
filmy[-1].save()
print(filmy)

mydb.commit()
cursor.close()
mydb.close()
