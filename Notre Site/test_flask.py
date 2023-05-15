from flask import Flask,render_template,request

app = Flask(__name__)


@app.route('/')

def index():
    return "This is a page"

@app.route('/about')

def about():

  return "<p>Une autre page</p>"

@app.route('/resultat',methods = ['POST'])

def resultat():

  result = request.form

  n = result['nom']

  p = result['prenom']

  return render_template("resultats.html", nom=n, prenom=p) # génère la page html avec les paramètres nom et prenom

##################################################################################

app.run(debug=True,port = 8085, host = '0.0.0.0')