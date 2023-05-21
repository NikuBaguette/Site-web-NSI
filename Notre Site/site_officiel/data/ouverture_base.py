import sqlite3
from faker import Faker
import random

fake=Faker(local='fr_FR')
con=sqlite3.connect('personne.db')
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS Personne(ID_personne INT PRIMARY KEY,Nom TEXT,Email TEXT,Adresse TEXT,Ville TEXT,Code_postal INT,Note INT,ID_jeux INT)")
cur.execute("CREATE TABLE IF NOT EXISTS Jeux(ID_Jeux INT PRIMARY KEY,Nom TEXT,Date_sortie TEXT,Note INT)")

sql = 'DELETE FROM Personne'
sql1 = 'DELETE FROM Jeux'
cur.execute(sql)
cur.execute(sql1)
con.commit()


listejeux=[("minecraft","18 novembre 2011"),("valorant","2 juin 2020"),("Apex","4 février 2019"),("Roblox","1 septembre 2006"),("CSGO","21 août 2012"),("smash bros","7 décembre 2018"),("GTAV","17 septembre 2013"),("Fortnite","21 juillet 2017"),("super mario odyssey","27 octobre 2017"),("cyberpunk 2077","10 décembre 2020")]
data=[]
data2=[]

for i in range(40):
      temp1=(i+1,fake.name(),fake.email(),fake.street_address(),fake.city(),fake.postcode(),random.randint(0,10),random.randint(1,10))
      data.append(temp1)
cur.executemany("INSERT INTO Personne VALUES(?, ?, ?, ?, ?, ?, ?, ?)", data)
con.commit()

for i in range(10):
      cur.execute(f"Select AVG(note) from Personne where id_jeux={i+1}")
      note=cur.fetchall()[0][0]
      if note == None:
            note=0
      note=round(note)
      temp2 = (i+1, listejeux[i][0], listejeux[i][1], note)
      data2.append(temp2)
cur.executemany("INSERT INTO JEUX VALUES(?, ?, ? ,?)", data2)
con.commit()


cur.close()
con.close()