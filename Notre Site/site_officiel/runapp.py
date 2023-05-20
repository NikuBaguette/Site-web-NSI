from flask import Flask, render_template, request
from os import path
import sqlite3
import templates
import data.sqlite_select


app = Flask(__name__)
info = data.sqlite_select.find()

@app.route("/")

def index():
    if path.exists("templates\\index.html") != False :
        return render_template("index.html")
    else:
        return "La page d'index s'affichera lorsqu'elle sera renseigné dans le dossier templates \n sous le nom de index.html"

@app.route("/result")

def result():
    if path.exists("templates\\result.html") != False :
        return render_template("result.html")
    else:
        return """<p> La page de résultat s'affichera lorsqu'elle sera renseigné dans le dossier templates <p/> <p> sous le nom de result.html <p/> <p>
        maximum : {} avec {}, minimum : {} avec {}, la moyenne est de {} <p/>""".format(info["maximum"][0][0], info["maximum"][0][1], info["minimum"][0][0], info["minimum"][0][1], info["moyenne"][0][0])

app.run(debug=True, host='0.0.0.0', port=5000)