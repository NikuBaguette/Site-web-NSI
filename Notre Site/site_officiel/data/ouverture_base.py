import sqlite3
from faker import Faker
import random

fake = Faker(local='fr_FR')
liste_avis = ["Trop Nul", "BOF", "Bien", "Tres bien"]

def creer_table_personne():
      con = sqlite3.connect('personne.db', check_same_thread=False)
      cur = con.cursor()
      cur.execute("CREATE TABLE IF NOT EXISTS Personne(ID_personne INT PRIMARY KEY,Nom TEXT,Email TEXT,Adresse TEXT,Ville TEXT,Code_postal INT,Note INT,Avis_jeux TEXT,ID_jeux INT)")
      sql = 'DELETE FROM Personne'
      cur.execute(sql)
      con.commit()
      cur.close()
      con.close()

def ajouter_une_vrai_personne(liste):
      con = sqlite3.connect('personne.db', check_same_thread=False)
      cur = con.cursor()
      cur.execute("Select count(nom) from Personne")
      con.commit()
      indice = cur.fetchall()[0][0]+1
      note=liste[5]
      if note <= 3:
            avis = liste_avis[0]
      elif note <= 5:
            avis = liste_avis[1]
      elif note <= 7:
            avis = liste_avis[2]
      else:
            avis = liste_avis[3]
      data=[indice,liste[0],liste[1],liste[2],liste[3],liste[4],liste[5],avis,liste[6]]
      cur.execute(f"INSERT INTO Personne Values(?,?,?,?,?,?,?,?,?)",data)
      con.commit()
      cur.close()
      con.close()

def ajouter_des_faux_gens(nombre: int):
      con = sqlite3.connect('personne.db', check_same_thread=False)
      cur = con.cursor()
      data = []
      for i in range(nombre):
            note = random.randint(0, 10)
            jeux = random.randint(1, 10)
            if jeux == 1:
                  note = random.randint(7,10)
            if note <= 3:
                  avis = liste_avis[0]
            elif note <= 5:
                  avis = liste_avis[1]
            elif note <= 7:
                  avis = liste_avis[2]
            else:
                  avis = liste_avis[3]
            
            temp1 = (i + 1, fake.name(), fake.email(), fake.street_address(), fake.city(), fake.postcode(), note, avis,jeux)
            data.append(temp1)
      cur.executemany("INSERT INTO Personne VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", data)
      con.commit()
      cur.close()
      con.close()

def creer_table_jeux():
      con = sqlite3.connect('personne.db', check_same_thread=False)
      cur = con.cursor()
      listejeux = [("Minecraft", "18 novembre 2011"), ("Valorant", "2 juin 2020"), ("Apex", "4 février 2019"),
                   ("Roblox", "1 septembre 2006"), ("CS:GO", "21 août 2012"), ("Super Smash Bros Ultimate", "7 décembre 2018"),
                   ("GTA V", "17 septembre 2013"), ("Fortnite", "21 juillet 2017"),
                   ("Super Mario Odyssey", "27 octobre 2017"), ("Cyberpunk 2077", "10 décembre 2020")]
      liste_avis = ["Trop Nul", "BOF", "Bien", "Tres bien"]
      cur.execute("CREATE TABLE IF NOT EXISTS Jeux(ID_Jeux INT PRIMARY KEY,Nom TEXT,Date_sortie TEXT,Note INT,Avis_jeux TEXT)")
      sql1 = 'DELETE FROM Jeux'
      cur.execute(sql1)
      con.commit()
      data2=[]
      for i in range(10):
            cur.execute(f"Select AVG(note) from Personne where id_jeux={i+1}")
            note=cur.fetchall()[0][0]
            if note == None:
                  note = 0
            note = round(note)
            if note <= 3:
                  avis = liste_avis[0]
            elif note <= 5:
                  avis = liste_avis[1]
            elif note <= 7:
                  avis = liste_avis[2]
            else:
                  avis = liste_avis[3]
            temp2 = (i+1, listejeux[i][0], listejeux[i][1], note,avis)
            data2.append(temp2)
      cur.executemany("INSERT INTO JEUX VALUES(?, ?, ? ,?, ?)", data2)
      con.commit()
      cur.close()
      con.close()