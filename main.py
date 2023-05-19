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
    return f"Films: id: {self.id} Title: {self.title} Year:{self.year}"

  def __repr__(self):
    return str(self)

  def save(self):
    query = "SELECT * FROM Films WHERE id_film = " + str(self.id)
    cursor.execute(query)
    row = cursor.fetchone()
    if row is None:
     query = "INSERT INTO Films(title, year) VALUE( " \
     "'" + self.title + "', " \
     "'" + self.year + "') "
     cursor.execute(query)


  def all():
    list = []
    cursor.execute("SELECT * FROM Films")
    for A in cursor:
      list.append(Film(A[0], A[1], A[2]))
    return list

def add(list, title, year):
    list.append(Film(list[-1].id + 1, title, year))

films = Film.all()

x="1"
while(x=="1" or x=="2"):
  x = input("Instrukcja:\n"
            "1-dodaj film\n"
            "2-pokaż obecną bazę danych\n"
            "inna liczba - wyłącz program\n")
  if(x=="1"):
    t=input("Podaj tytuł")
    r=input("Podaj rok")
    add(films, str(t), str(r))      ## przykładowe dodanie nowego filmu
    films[-1].save()                ## dzięki temu zapisujemy zmiany w bazie danych na serwerze


  if(x=="2"):
    films = Film.all()
    for a in range(len(films)):
      print(films[a])


mydb.commit()
cursor.close()
mydb.close()
