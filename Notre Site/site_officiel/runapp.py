from flask import Flask, render_template, request
from os import path
import sqlite3
import templates
import data.ouverture_base as ringuede

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
    ringuede.creer_table_personne(values)
    ringuede.creer_table_jeux()
    return render_template("result.html")

app.run(debug=True, host='0.0.0.0', port=5000)