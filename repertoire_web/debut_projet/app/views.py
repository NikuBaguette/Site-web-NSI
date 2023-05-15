# coding: utf8
from app import app
from flask import render_template, Flask, request, redirect, url_for
import sqlite3



@app.route('/')
def main( nom = None ):
   return render_template( 'main.html' )

@app.route('/edit/name')
def edit_name():
   return render_template( 'edit_nom.html' )

@app.route('/save/name', methods=['GET','POST'] )
def save_name():
   with sqlite3.connect('repertoire.db') as db:
    	print("Base élèves ouverte avec succès")  
    	db.execute("""
    	CREATE TABLE IF NOT EXISTS personne (
       	id INTEGER PRIMARY KEY AUTOINCREMENT,
       	prenom TEXT, 
       	nom TEXT, 
       	email TEXT
       	)
       	""")
   if request.method == 'POST':
      try:
         prenom = request.form['prenom']
         nom = request.form['nom']
         email = request.form['email']
               
         with sqlite3.connect("./repertoire.db") as db:
            cur = db.cursor()
            cur.execute(
               "INSERT INTO personne (prenom, nom,  email) VALUES (?,?,?)",
               (prenom, nom, email)
               )
            db.commit()
            msg = f"la personne {nom} {prenom} a été enregistré avec succès"
      except Exception as e:
         db.rollback() # on ne tient pas compte de ce qui a été entré
         msg = f"{e} (la personne n'a pu être enregistrée)"
      finally:
         return render_template("resultat.html",msg = msg)    

# moteur de recherche
@app.route('/recherche')
def new_recherche():
   return render_template('recherche.html')

@app.route('/requete', methods = ['POST', 'GET'])
def requete():
   
   if request.method == 'POST':
      try:
         champ = request.form['champ']
         requete = request.form['motcle']
         
         
         requete2 = f"SELECT * FROM personne WHERE {champ} = '{requete}' "
        
         with sqlite3.connect("./repertoire.db") as db:
            db.row_factory = sqlite3.Row # pour que les lignes soient sous la forme d'un dictionnaire 
            cur = db.cursor()
            
            cur.execute(requete2)
            #cur.execute(f"SELECT * FROM personne WHERE {champ} LIKE ?", (requete,))
            # ou cur.execute("SELECT * FROM eleves WHERE nom LIKE " + str(rekete) si vous voulez jouer avec Little Bob
            res = cur.fetchall();
            for t in cur:
               print(t)
            
            l = len(res)
            msg = "Requête OK"
            
      except Exception as e:
         msg = f"{e} (la requête n'a pu être exécutée)"
         res = "Pas de résultat"
         l = 0
      finally:
         return render_template("requete.html",msg = msg, res = res, l = l, reqete = requete2, champ = champ )

# on ouvre un serveur en local sur le port 8000
