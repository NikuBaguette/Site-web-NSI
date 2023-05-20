import sqlite3

conn=sqlite3.connect("data\\personne.db")
cur=conn.cursor()

def find():
    
    cur.execute("SELECT Nom,min(note) FROM Personne")
    conn.commit()
    minimum = cur.fetchall()
    cur.execute("Select Avg(note) From Personne")
    conn.commit()
    moyenne = cur.fetchall()
    cur.execute("Select Nom,max(note) From Personne")
    conn.commit()
    maximum = cur.fetchall()
    cur.close()
    conn.close()
    return {"minimum" : minimum, "maximum" : maximum, "moyenne" : moyenne}