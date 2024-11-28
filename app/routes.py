# app/routes.py

from app import app
from flask import request
from flask import render_template

import networkx as nx

items = []

@app.route('/')
def hello():
    return "Hello, AXXONN!"

@app.route('/hello2')
def hello2():
    return "Hello2, AXXONN!"

@app.route('/items', methods=['GET'])
def get_items():
    return {'items': items}

def bigram_edges(tokens):
    edgetable = list(zip(tokens[:-1], tokens[1:]))
    return edgetable


@app.route('/net')
def viewnetwork():
    keywords_nodes = []

    tokens = ['bilbo', 'baggin', 'bagend', 'announce', 'shortly', 'celebrate', 'eleventy', 'birthday', 'party', 'special', 'magnificence', 'talk', 'excitement', 'hobbiton', 'bilbo', 'rich', 'peculiar', 'wonder', 'shire', 'year', 'remarkable', 'disappearance', 'unexpected', 'return', 'rich', 'bring', 'travel', 'local', 'legend', 'popularly', 'believe', 'old', 'folk', 'hill', 'bagend', 'tunnel', 'stuff', 'treasure', 'fame', 'prolong', 'vigour', 'marvel', 'time', 'wear', 'little', 'effect', 'baggin', 'ninety', 'ninety', 'begin', 'preserve', 'unchanged', 'nearer', 'mark', 'shake', 'head', 'think', 'good', 'thing', 'unfair', 'possess', 'apparently', 'perpetual', 'youth', 'reputedly', 'inexhaustible', 'wealth', 'pay', 'say', 'not', 'natural', 'trouble', 'come', 'far', 'trouble', 'come', 'baggin', 'generous', 'money', 'people', 'willing', 'forgive', 'oddity', 'good', 'fortune', 'remain', 'visit', 'term', 'relative', 'course', 'sackville', 'bagginse', 'devoted', 'admirer', 'hobbit', 'poor', 'unimportant', 'family', 'close', 'friend', 'young', 'cousin', 'begin', 'grow', 'eld', 'bilbos', 'favourite', 'young', 'frodo', 'baggin', 'bilbo', 'ninety', 'adopt', 'frodo', 'heir', 'bring', 'live', 'bagend', 'hope', 'sackvillebagginse', 'finally', 'dash', 'bilbo', 'frodo', 'happen', 'birthday', 'september', '22nd', 'well', 'come', 'live', 'frodo', 'lad', 'say', 'bilbo', 'day', 'celebrate', 'birthday', 'party', 'comfortably', 'time', 'frodo', 'tweens', 'hobbit', 'call', 'irresponsible', 'twenty', 'childhood', 'come', 'age', 'thirty']

    edgetable = bigram_edges(tokens)

    return "NETWORK, AXXONN!"

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

@app.route('/web1')
def web1():
    render_template('web1.html')

@app.route('/web0')
def web0():
    render_template('web0.html')








# @app.route('/web0')
# def web0():
#     render_template('web0.html', content="Hello World WEB0!")

# @app.route('/web1')
# def web1():
#     render_template('web1.html', content="Hello World WEB1!")



# @app.route('/web11')
# def web11():
#     render_template('web11.html')

# @app.route('/web00')
# def web00():
#     render_template('web00.html')
