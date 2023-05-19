from flask import Flask, render_template, request
from os import path
import templates
app = Flask(__name__)

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
        return "La page de résultat s'affichera lorsqu'elle sera renseigné dans le dossier templates \n sous le nom de result.html"

app.run(debug=True, host='0.0.0.0', port=5000)
