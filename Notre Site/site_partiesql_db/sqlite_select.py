import sqlite3

conn=sqlite3.connect("personne.db")
cur=conn.cursor()


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
print(f"minimum = {minimum}")
print(f"moyenne = {moyenne}")
print(f"maximum = {maximum}")