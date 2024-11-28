# app/routes.py

from app import app
from flask import request
from flask import render_template

import networkx as nx

items = []

# @app.route('/')
# def home():
#    return render_template('index.html')

@app.route('/')
def home():
    return "HOME: Hello, AXXONN!"

@app.route('/web')
def web():
   return render_template('app/index.html')

@app.route('/hello')
def hello():
    return "Hello, AXXONN!"

@app.route('/items', methods=['GET'])
def get_items():
    return {'items': items}

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    if item_id < len(items):
        return {'item': items[item_id]}
    else:
        return {'error': 'Item not found'}, 404

@app.route('/items', methods=['POST'])
def add_item():
    item = request.get_json()
    items.append(item)
    return {'message': 'Item added successfully'}, 201


def bigram_edges(tokens):
    edgetable = list(zip(tokens[:-1], tokens[1:]))
    return edgetable

@app.route('/net')
def net():
    keywords_nodes = []

    tokens = ['bilbo', 'baggin', 'bagend']

    edgetable = bigram_edges(tokens)

    return "NETWORK"
