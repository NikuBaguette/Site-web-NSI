import sqlite3

conn = sqlite3.connect("personne.db")
cur = conn.cursor()
cur.execute("Select count(nom) from Personne")
conn.commit()
nombre=cur.fetchall()
print(nombre)
def find():
    cur.execute("SELECT Nom,min(note) FROM Jeux")
    conn.commit()
    minimum = cur.fetchall()[0]
    cur.execute("Select Avg(note) From Jeux")
    conn.commit()
    moyenne = cur.fetchall()[0][0]
    cur.execute("Select Nom,max(note) From Jeux")
    conn.commit()
    maximum = cur.fetchall()[0]
    cur.close()
    conn.close()
    return {"minimum": minimum, "maximum": maximum, "moyenne": moyenne}

print(find())