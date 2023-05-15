import sqlite3

conn = sqlite3.connect('baseAvecPython.db')
cur = conn.cursor()

cur.execute('SELECT * FROM LIVRES')
liste = cur.fetchall()
recherche = (1960, 8)

cur.execute('SELECT titre FROM LIVRES WHERE ann_publi < ? AND note > ?', recherche)
conn.commit()

liste1 = cur.fetchall()

cur.close()
conn.close()
print(f"liste = {liste}")
print(f"liste1 = {liste1}")