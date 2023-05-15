import sqlite3
conn = sqlite3.connect('baseAvecPython.db')
cur = conn.cursor()

datas = [
	(1,'1984','Orwell',1949,10),
	(2,'Dune','Herbert',1965,8),
	(3,'Fondation','Asimov',1951,9),
	(4,'Le meilleur des mondes','Huxley',1931,7),
	(5,'Fahrenheit 451','Bradbury',1953,7),
	(6,'Ubik','K.Dick',1969,9),
	(7,'Chroniques martiennes','Bradbury',1950,8),
	(8,'La nuit des temps','Barjavel',1968,7),
	(9,'Blade Runner','K.Dick',1968,8),
	(10,'Les Robots','Asimov',1950,9),
	(11,'La Planète des singes','Boulle',1963,8),
	(12,'Ravage','Barjavel',1943,8),
	(13,'Le Maître du Haut Château','K.Dick',1962,8),
	(14,'Le monde des Ā','Van Vogt',1945,7),
	(15,'La Fin de l’éternité','Asimov',1955,8),
	(16,'De la Terre à la Lune','Verne',1865,10)
 ]


#cur.execute("CREATE TABLE LIVRES(id INT, titre TEXT, auteur TEXT, ann_PUBLI INT, note INT ")
cur.execute("CREATE TABLE IF NOT EXISTS LIVRES(id INT, titre TEXT, auteur TXT, ann_publi INT, note INT)")
cur.executemany("INSERT INTO LIVRES(id,titre,auteur,ann_publi,note) VALUES(?, ?, ?, ?, ?)", datas)
conn.commit()
cur.close()
conn.close()
