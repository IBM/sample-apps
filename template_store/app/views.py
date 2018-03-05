"""Licensed Materials - Property of IBM
5725I71-CC011829
(C) Copyright IBM Corp. 2017, 2018. All Rights Reserved.
US Government Users Restricted Rights - Use, duplication or
disclosure restricted by GSA ADP Schedule Contract with IBM Corp."""
__author__ = 'IBM'



import os
import sqlite3
from contextlib import closing

from app import app
from flask import g
# 0. all my imports
from flask import render_template, request, redirect, url_for

from qpylib import qpylib

# 1. configuration for db store
DATABASE = '/store/mystore.db'

# 2. initialise db config, for flask
app.config.from_object(__name__)

# 3. define functions for connecting and starting the db
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('db/schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

# 4. invoked db initialisation
def start_db():
    if os.path.isfile(app.config['DATABASE']):
        qpylib.log("mystore db file exists, do nothing ...")
    else:
        qpylib.log("mystore db file does not exist, starting db creation and initialisation")
        init_db()

start_db()

# 5. request handlers to open and close a db connection before and after each request
#  make sure these coded logically after the init_db function
@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

###
### the routes for my storage app
###

@app.route('/')
@app.route('/index')
def show_entries():
    qpylib.log("show_entries()>>>")
    cur = g.db.execute('select title, text from entries order by id desc')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    qpylib.log("show_entries() 1>>>")
    return render_template('show_entries.html', entries=entries)

@app.route('/add_entry', methods=['POST'])
def add_entry():
    qpylib.log("add_entry()>>>")
    g.db.execute('insert into entries (title, text) values (?, ?)',
                 [request.form['title'], request.form['text']])
    g.db.commit()
    return redirect(url_for('show_entries'), code=303)
