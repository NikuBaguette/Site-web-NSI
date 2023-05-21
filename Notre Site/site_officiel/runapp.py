from flask import Flask, render_template, request
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

@app.route("/", methods = ["GET", "POST"])

def index():

    return render_template("index.html")


@app.route("/result", methods = ["GET", "POST"])

def result():
    username = request.form['username']
    email = request.form['email']
    adresse = request.form['adresse']
    ville = request.form['ville']
    CP = int(request.form['CP'])
    game = request.form['game']
    for i in range(10):
        if game == listejeux[i]:
            game = i + 1
    note = float(request.form['note'])
    values = [username, email, adresse, ville, CP, note, game]
    ouverture.creer_table_personne(values)
    ouverture.creer_table_jeux()
    minimum = requete.find_min()[1]
    nom_minimum=requete.find_min()[0]
    maximum= requete.find_maxi()[1]
    nom_maximum=requete.find_maxi()[0]

    #minecraft
    nom_minecraft=requete.find_Minecraft()[1]
    date_minecraft=requete.find_Minecraft()[2]
    note_minecraft=requete.find_Minecraft()[3]
    avis_minecraft = requete.find_Minecraft()[4]

    #Valorant
    nom_Valorant = requete.find_Valorant()[1]
    date_Valorant = requete.find_Valorant()[2]
    note_Valorant = requete.find_Valorant()[3]
    avis_Valorant = requete.find_Valorant()[4]

    #Apex
    nom_Apex = requete.find_Apex()[1]
    date_Apex = requete.find_Apex()[2]
    note_Apex = requete.find_Apex()[3]
    avis_Apex = requete.find_Apex()[4]

    #Roblox
    nom_Roblox = requete.find_Roblox()[1]
    date_Roblox = requete.find_Roblox()[2]
    note_Roblox= requete.find_Roblox()[3]
    avis_Roblox = requete.find_Roblox()[4]

    #CSGO
    nom_CSGO = requete.find_CSGO()[1]
    date_CSGO = requete.find_CSGO()[2]
    note_CSGO = requete.find_CSGO()[3]
    avis_CSGO = requete.find_CSGO()[4]

    #Smash_bros
    nom_Smash_bros = requete.find_Smash_bros()[1]
    date_Smash_bros = requete.find_Smash_bros()[2]
    note_Smash_bros= requete.find_Smash_bros()[3]
    avis_Smash_bros= requete.find_Smash_bros()[4]

    #GTAV
    nom_GTAV = requete.find_GTAV()[1]
    date_GTAV = requete.find_GTAV()[2]
    note_GTAV = requete.find_GTAV()[3]
    avis_GTAV = requete.find_GTAV()[4]

    #Fortnite
    nom_Fortnite = requete.find_Fortnite()[1]
    date_Fortnite = requete.find_Fortnite()[2]
    note_Fortnite = requete.find_Fortnite()[3]
    avis_Fortnite = requete.find_Fortnite()[4]

    #Super_mario_odyssey
    nom_Super_mario_odyssey = requete.find_Super_mario_odyssey()[1]
    date_Super_mario_odyssey = requete.find_Super_mario_odyssey()[2]
    note_Super_mario_odyssey = requete.find_Super_mario_odyssey()[3]
    avis_Super_mario_odyssey = requete.find_Super_mario_odyssey()[4]
    
    #Cyberpunk
    nom_Cyberpunk = requete.find_Cyberpunk()[1]
    date_Cyberpunk= requete.find_Cyberpunk()[2]
    note_Cyberpunk = requete.find_Cyberpunk()[3]
    avis_Cyberpunk = requete.find_Cyberpunk()[4]

    return render_template("result.html", username = username, minimum=minimum,nom_minimum=nom_minimum,maximum=maximum,nom_maximum=nom_maximum,
                           nom_minecraft=nom_minecraft,date_minecraft=date_minecraft,note_minecraft=note_minecraft,avis_minecraft=avis_minecraft,
                           nom_Valorant=nom_Valorant,date_Valorant =date_Valorant,note_Valorant=note_Valorant,avis_Valorant=avis_Valorant,
                           nom_Apex=nom_Apex,date_Apex=date_Apex,note_Apex=note_Apex,avis_Apex=avis_Apex,
                           nom_Roblox=nom_Roblox,date_Roblox=date_Roblox,note_Roblox=note_Roblox,avis_Roblox=avis_Roblox,
                           nom_CSGO=nom_CSGO,date_CSGO=date_CSGO,note_CSGO=note_CSGO,avis_CSGO=avis_CSGO,
                           nom_Smash_bros=nom_Smash_bros,date_Smash_bros=date_Smash_bros,note_Smash_bros=note_Smash_bros,avis_Smash_bros=avis_Smash_bros,
                           nom_GTAV=nom_GTAV,date_GTAV=date_GTAV,note_GTAV=note_GTAV,avis_GTAV=avis_GTAV,
                           nom_Fortnite=nom_Fortnite,date_Fortnite=date_Fortnite,note_Fortnite=note_Fortnite,avis_Fortnite=avis_Fortnite,
                           nom_Super_mario_odyssey=nom_Super_mario_odyssey,date_Super_mario_odyssey=date_Super_mario_odyssey,note_Super_mario_odyssey=note_Super_mario_odyssey,avis_Super_mario_odyssey=avis_Super_mario_odyssey,
                           nom_Cyberpunk=nom_Cyberpunk,date_Cyberpunk=date_Cyberpunk,note_Cyberpunk=note_Cyberpunk,avis_Cyberpunk=avis_Cyberpunk)


app.run(debug=True, host='0.0.0.0', port=5000)