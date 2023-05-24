import sqlite3
from faker import Faker
import random

fake = Faker(local='fr_FR')
liste_avis = [("Graphismes du jeu inexistant, personnages et antagonistes pas interessants. Ce jeu est une insulte envers les joueurs","L'aventure donné était ininteressante ! Je me suis endormie devant ce jeu. J'ai même fait jouer mon enfant à ce jeu, ses premiers mots étaient 'arrête ça stp'"),
 ("Pourquoi les développeurs ont fait ce jeu, c'est pour moi l'épisode de trop, les précedents étaient mieux","Le début du jeu est bien mais uniquement le début, après le tutorielle le jeu crash et mon pc a explosé !"),
 ("Un princippe interessant mais mal utilisé, les bugs sont trop fréquent et la sécurite contre les tricheurs est trop faible","Je me suis fait spawn kill par titouanDu92 si vous le connaissez, donnez-moi son adresse je vais le tabasser"),
 ("Malgré une histoire intéressante le game-designe n'est pas là, je suis déçu de ce jeu ","J'aurais aimé apprecier à sa juste valeur ce jeu qui a apparement des graphismes exceptionnelles mais bon je suis aveugle"),
 ("Un jeu moyen sans plus, il n'a pas de réel défaut n'y de qualité. Il est juste OK","Une communauté soudé mais c'est un jeu qui n'est pas fini dont on fait vite le tour. Dommage !"),
 ("Quelques défauts mais qui peuvent être réglés par des patchs, hâte de voir le jeu évoluer","Un jeu très intéressant mais vraiment trop court, le personnage principal est bien écrit mais qui est accompagné par des personnages secondaires inintéressants"),
 ("Un jeu amusant et très interessant même si il manque quelque chose pour en faire un vrai bon jeu","Un jeu incroyable mais le online à la ramasse. Dommage il ne manquait que ca pour en faire un bon jeu"),
 ("Le jeu est très bien avec un contenu émoustillant","Alors là je suis content ce jeu est bien avec plus de 100 heures de gameplay même si pour y acceder il faut payer, heureusement que je suis riche."),
 ("C'est un bon jeu de type sandbox, un jeu familial qui peut plaire à tout le monde","C'est bien, j'aime bien, tu aimes bien et si t'aime pas je te tabasse"),
 ("j'aime beaucoup ce jeu car ça me permet d'oublier ma vie pourrie (j'ai perdu mon travail, ma femme, mes enfants et mes parents)", "Jeu incroyable et riche en expérience, on sent qu'il va avoir du mal à veillir et ça fait plaisir."),
 ("Un jeu parfait d'une durée de vie et possibilités infinie, très amusant, un multijoueur parfait. Bravo !!!","C'est vraiment trop bien, je joue avec mes copains de l'ecole et je sui le plus fors meme ci ma momman es pas tres contentes quands j'y jouet.")]

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
      data=[indice,liste[0],liste[1],liste[2],liste[3],liste[4],liste[5],liste[6],liste[7]]
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
            indice=random.randint(0,1)
            avis = liste_avis[note][indice]
            temp1 = (i + 1, fake.name(), fake.email(), fake.street_address(), fake.city(), fake.postcode(), note, avis, jeux)
            data.append(temp1)
      cur.executemany("INSERT INTO Personne VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", data)
      con.commit()
      cur.close()
      con.close()

def creer_table_jeux():
      con = sqlite3.connect('personne.db', check_same_thread=False)
      cur = con.cursor()
      listejeux = [("Minecraft", "18 novembre 2011", "Minecraft-Logo.png"), ("Valorant", "2 juin 2020", "valorant.png"), ("Apex", "4 février 2019", "Apex-Legends-Logo-2019.png"),
                   ("Roblox", "1 septembre 2006", "roblox.png"), ("CS:GO", "21 août 2012", "csgo.png"), ("Super Smash Bros Ultimate", "7 décembre 2018", "Super_Smash_Bros._Ultimate_Logo.png"),
                   ("GTA V", "17 septembre 2013", "gta.png"), ("Fortnite", "21 juillet 2017", "fornite.png"),
                   ("Super Mario Odyssey", "27 octobre 2017", "supermario.jpg"), ("Cyberpunk 2077", "10 décembre 2020", "téléchargé.png")]
      
      cur.execute("CREATE TABLE IF NOT EXISTS Jeux(ID_Jeux INT PRIMARY KEY,Nom TEXT,Date_sortie TEXT,Note INT,Avis_jeux TEXT, lien TEXT)")
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
            indice=random.randint(0,1)
            avis = liste_avis[note][indice]
            temp2 = (i+1, listejeux[i][0], listejeux[i][1], note, avis, listejeux[i][2])
            data2.append(temp2)
      cur.executemany("INSERT INTO JEUX VALUES(?, ?, ? ,?, ?, ?)", data2)
      con.commit()
      cur.close()
      con.close()
