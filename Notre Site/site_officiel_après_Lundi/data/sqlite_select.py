import sqlite3

def find_min():
    conn = sqlite3.connect("personne.db", check_same_thread=False)
    cur = conn.cursor()
    cur.execute("SELECT Nom,min(note) FROM Jeux")
    conn.commit()
    minimum = cur.fetchall()[0]
    cur.close()
    conn.close()
    return  minimum

def find_moyenne():
    conn = sqlite3.connect("personne.db", check_same_thread=False)
    cur = conn.cursor()
    cur.execute("Select Avg(note) From Jeux")
    conn.commit()
    moyenne = cur.fetchall()[0][0]
    cur.close()
    conn.close()
    return moyenne

def find_maxi():
    conn = sqlite3.connect("personne.db", check_same_thread=False)
    cur = conn.cursor()
    cur.execute("Select Nom,max(note) From Jeux")
    conn.commit()
    maximum = cur.fetchall()[0]
    cur.close()
    conn.close()
    return maximum

def find_Game(id: int): # je te ez Lucien
    conn = sqlite3.connect("personne.db", check_same_thread=False)
    cur = conn.cursor()
    cur.execute(f"Select * from Jeux where ID_jeux={id}")
    conn.commit()
    result = cur.fetchall()[0]
    cur.close()
    conn.close()
    return result

def find_personne(id):
    conn = sqlite3.connect("personne.db", check_same_thread=False)
    cur = conn.cursor()
    cur.execute(f"Select Nom, note, Avis_jeux from personne where ID_jeux={id}")
    conn.commit()
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result
