#!/usr/bin/env python
# coding: utf8
ADRESSE_IP ="127.0.0.1"
from app import app
#définir l'adresse du serveur web
app.run( debug=True, host=ADRESSE_IP, port=5000 )
# Production
#app.run( host='0.0.0.0' )  
