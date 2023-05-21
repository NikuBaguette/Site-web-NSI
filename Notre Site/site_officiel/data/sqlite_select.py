import sqlite3

conn = sqlite3.connect("personne.db", check_same_thread=False)
cur = conn.cursor()

def find_min():
    cur.execute("SELECT Nom,min(note) FROM Jeux")
    conn.commit()
    minimum = cur.fetchall()[0]
    return  minimum

def find_moyenne():
    cur.execute("Select Avg(note) From Jeux")
    conn.commit()
    moyenne = cur.fetchall()[0][0]
    return moyenne

def find_maxi():
    cur.execute("Select Nom,max(note) From Jeux")
    conn.commit()
    maximum = cur.fetchall()[0]
    return maximum

def find_Game(id: int): # je te ez Lucien
    cur.execute(f"Select * from Jeux where ID_jeux={id}")
    conn.commit()
    result = cur.fetchall()[0]
    return result
