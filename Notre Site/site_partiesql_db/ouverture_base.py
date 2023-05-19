import sqlite3
from faker import Faker
import random

fake=Faker(local='fr_FR')
con=sqlite3.connect('personne.db')
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS Personne(Nom TEXT,Email TEXT,Adresse TEXT,Ville TEXT,Code_postal INT,Note INT)")

sql = 'DELETE FROM Personne'
cur.execute(sql)
con.commit()

data=[]
for _ in range(10):
    un=(fake.name(),fake.email(),fake.street_address(),fake.city(),fake.postcode(),random.randint(0,20))
    data.append(un)

cur.executemany("INSERT INTO Personne VALUES(?, ?, ?, ?, ?, ?)", data)
con.commit()
cur.close()
con.close()