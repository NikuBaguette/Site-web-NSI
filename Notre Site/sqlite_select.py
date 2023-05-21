import sqlite3

conn = sqlite3.connect("personne.db")
cur = conn.cursor()

def find():
    cur.execute("SELECT Nom,min(note) FROM Jeux")
    conn.commit()
    minimum = cur.fetchall()
    cur.execute("Select Avg(note) From Jeux")
    conn.commit()
    moyenne = cur.fetchall()
    cur.execute("Select Nom,max(note) From Jeux")
    conn.commit()
    maximum = cur.fetchall()
    cur.close()
    conn.close()
    return {"minimum": minimum, "maximum": maximum, "moyenne": moyenne}

print(find())