"""Licensed Materials - Property of IBM
5725I71-CC011829
(C) Copyright IBM Corp. 2017, 2018. All Rights Reserved.
US Government Users Restricted Rights - Use, duplication or
disclosure restricted by GSA ADP Schedule Contract with IBM Corp."""
__author__ = 'IBM'



from flask import Response
from app import app
from qpylib.qpylib import log
from qpylib.json_qpylib import json_html
from qpylib.offense_qpylib import get_offense_json_html
from qpylib.asset_qpylib import get_asset_json_html


def response_json_html(text):
    return response_json(json_html('<strong>' + text + '</strong>'))


def response_json(json):
    return Response(response=json, status=200, mimetype='application/json')

# =========================================================================================
# Dashboard
# =========================================================================================


@app.route('/dashboard', methods=['GET'])
def dashboard():
    return response_json_html('Dashboard custom content')

# =========================================================================================
# Offenses - My Offenses
# =========================================================================================


@app.route('/offensemylistheader', methods=['GET'])
def offensemylistheader():
    return response_json_html('My Offenses header custom content')


@app.route('/offensemylistfooter', methods=['GET'])
def offensemylistfooter():
    return response_json_html('My Offenses footer custom content')

# =========================================================================================
# Admin
# =========================================================================================


@app.route('/adminall', methods=['GET'])
def adminall():
    return response_json_html('Admin All Tabs custom content')
