import mysql.connector

mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  password='gerard_gruszka',
  port='3306',
  database='Films'
)

cursor = mydb.cursor()

class Film:
  def __init__(self, id, title, year):
    self.id = id
    self.title = title
    self.year = year

  def __str__ (self):
    return f"Filmy: id: {self.id} Title: {self.title} Year:{self.year}"

  def save(self):
    query = "SELECT * FROM Films WHERE id_film = " + str(self.id)
    cursor.execute(query)
    row = cursor.fetchone()
    if row is None:
     query = "INSERT INTO Films(title, year) VALUE( " \
     "'" + self.title + "', " \
     "'" + self.year + "') "
     cursor.execute(query)
    else:
      query = "UPDATE Films SET " \
      "id_film = " + str(self.id) + ", " \
      "title = '" + self.title + "', " \
      "year = '" + self.year + "', " \
      " WHERE id_film = " + str(self.id)
      cursor.execute(query)


  def all():
    list = []
    cursor.execute("SELECT * FROM Films")
    for A in cursor:
      list.append(Film(A[0], A[1], A[2]))
    return list

def add(list, title, year):
  list.append(Film(list[-1].id + 1, title, year))




filmy = Film.all()

add(filmy,"Prestige","2010")
filmy[-1].save()


mydb.commit()
cursor.close()
mydb.close()
