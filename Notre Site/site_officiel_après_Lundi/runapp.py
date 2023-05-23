from flask import Flask, render_template, request, redirect, url_for
from os import path
import sqlite3
import templates
import data.ouverture_base as ouverture
import data.sqlite_select as requete
listejeux = ["Minecraft", "Valorant", "Apex",
                   "Roblox", "CS:GO", "Super Smash Bros Ultimate",
                   "GTA 5", "Fortnite",
                   "Super Mario Odyssey", "Cyberpunk 2077"]

app = Flask(__name__)
ouverture.creer_table_personne()
ouverture.ajouter_des_faux_gens(30)
ouverture.creer_table_jeux()
img_path = path.join('static', 'images')

@app.route("/")
def direct():
    return redirect(url_for('index'))

@app.route("/index", methods = ["GET", "POST"])

def index():
    return render_template('index.html')

@app.route("/formulaire", methods = ["GET", "POST"])

def formulaire():
    return render_template("formulaire.html")


@app.route("/result", methods = ["GET", "POST"])

def result():
    username = request.form['username']
    email = request.form['email']
    adresse = request.form['adresse']
    ville = request.form['ville']
    game = request.form['game']
    avis= request.form['avis']
    for i in range(10):
        if game == listejeux[i]:
            game = i + 1
    note = float(request.form['note'])
    if request.form['CP'].isdigit() == False or " " not in username or "@" not in email:
        return redirect(url_for('index'))

    CP = int(request.form['CP'])

    values = [username, email, adresse, ville, CP, note,avis, game]
    ouverture.ajouter_une_vrai_personne(values)
    ouverture.creer_table_jeux()

    nom_minimum, minimum=requete.find_min()
    nom_maximum, maximum=requete.find_maxi()

    #minecraft
    id_minecraft, nom_minecraft, date_minecraft, note_minecraft, avis_minecraft, lien_minecraft = requete.find_Game(1)

    #Valorant
    id_Valorant, nom_Valorant, date_Valorant, note_Valorant, avis_Valorant, lien_Valorant = requete.find_Game(2)

    #Apex
    id_Apex, nom_Apex, date_Apex, note_Apex, avis_Apex, lien_Apex = requete.find_Game(3)

    #Roblox
    id_Roblox, nom_Roblox, date_Roblox, note_Roblox, avis_Roblox, lien_Roblox = requete.find_Game(4)

    #CSGO
    id_CSGO, nom_CSGO, date_CSGO, note_CSGO, avis_CSGO, lien_CSGO = requete.find_Game(5)

    #Smash_bros
    id_SSBU, nom_SSBU, date_SSBU, note_SSBU, avis_SSBU, lien_SSBU = requete.find_Game(6)

    #GTAV
    id_GTAV, nom_GTAV, date_GTAV, note_GTAV, avis_GTAV, lien_GTAV = requete.find_Game(7)

    #Fortnite
    id_Fortnite, nom_Fortnite, date_Fortnite, note_Fortnite, avis_Fortnite, lien_Fortinte = requete.find_Game(8)

    #Super_mario_odyssey
    id_Super_Mario_Odyssey, nom_Super_Mario_Odyssey, date_Super_Mario_Odyssey, note_Super_Mario_Odyssey, avis_Super_Mario_Odyssey, lien_Super_Mario_Odyssey = requete.find_Game(9)
    
    #Cyberpunk
    id_Cyberpunk, nom_Cyberpunk, date_Cyberpunk, note_Cyberpunk, avis_Cyberpunk, lien_Cyberpunk = requete.find_Game(10)

    return render_template("result.html", username = username, minimum = minimum, nom_minimum = nom_minimum, 
                           maximum = maximum, nom_maximum = nom_maximum,
                           nom_minecraft = nom_minecraft, date_minecraft = date_minecraft,
                           note_minecraft = note_minecraft, avis_minecraft = avis_minecraft,
                           nom_Valorant = nom_Valorant, date_Valorant = date_Valorant,
                           note_Valorant = note_Valorant, avis_Valorant = avis_Valorant,
                           nom_Apex = nom_Apex, date_Apex = date_Apex, note_Apex = note_Apex,
                           avis_Apex = avis_Apex, nom_Roblox = nom_Roblox, date_Roblox = date_Roblox,
                           note_Roblox = note_Roblox, avis_Roblox = avis_Roblox, nom_CSGO = nom_CSGO,
                           date_CSGO = date_CSGO, note_CSGO = note_CSGO, avis_CSGO = avis_CSGO,
                           nom_SSBU = nom_SSBU, date_SSBU = date_SSBU, note_SSBU = note_SSBU, avis_SSBU = avis_SSBU,
                           nom_GTAV = nom_GTAV, date_GTAV = date_GTAV, note_GTAV = note_GTAV, avis_GTAV = avis_GTAV,
                           nom_Fortnite = nom_Fortnite, date_Fortnite = date_Fortnite, note_Fortnite = note_Fortnite,
                           avis_Fortnite = avis_Fortnite, nom_Super_Mario_Odyssey = nom_Super_Mario_Odyssey, date_Super_Mario_Odyssey = date_Super_Mario_Odyssey,
                           note_Super_Mario_Odyssey = note_Super_Mario_Odyssey, avis_Super_Mario_Odyssey = avis_Super_Mario_Odyssey,
                           nom_Cyberpunk = nom_Cyberpunk, date_Cyberpunk = date_Cyberpunk, note_Cyberpunk = note_Cyberpunk,
                           avis_Cyberpunk = avis_Cyberpunk)

@app.route("/recherche", methods = ["GET", "POST"])

def recherche():
    if request.method == "POST":
        nom_game = request.form['game']
        for i in range(10):
            if nom_game == listejeux[i]:
                id_game = i + 1
        profils = requete.find_personne(id_game)
        len_profils = len(profils)
        id_game, nom_game, date_game, note_game, avis_game, lien_game = requete.find_Game(id_game)
        
        img_file = "images/"+lien_game
        
        image = url_for('static', filename = img_file)
        return render_template('recherche.html', nom_game = nom_game, id_game = id_game, profils = profils,
                           image = image, len_profils = len_profils,
                           date_game = date_game, note_game = note_game, avis_game = avis_game)
    return render_template('recherche.html')


app.run(debug = True, host='0.0.0.0', port=50069)
