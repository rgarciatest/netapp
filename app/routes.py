# app/routes.py

from app import app
from flask import request
from flask import render_template

import networkx as nx

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/hello')
def hello():
    return "Hello, AXXONN!"

def bigram_edges(tokens):
    edgetable = list(zip(tokens[:-1], tokens[1:]))
    return edgetable

@app.route('/net')
def net():
    keywords_nodes = []

    tokens = ['bilbo', 'baggin', 'bagend']

    edgetable = bigram_edges(tokens)

    return "NETWORK"
