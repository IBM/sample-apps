"""Licensed Materials - Property of IBM
5725I71-CC011829
(C) Copyright IBM Corp. 2017, 2018. All Rights Reserved.
US Government Users Restricted Rights - Use, duplication or
disclosure restricted by GSA ADP Schedule Contract with IBM Corp."""

from flask import render_template, jsonify, request
from app import app
from qpylib import qpylib
import json


# Store a reference to this apps UUID so we can filter it out of the app list later
with open('/app/manifest.json', 'r') as manifest:
    OWN_UUID = json.load(manifest).get('uuid')


@app.route('/')
@app.route('/index')
def index():
    return render_template("app_status_main.html")


@app.route('/apps', methods=['GET'])
def get_app_status_data():
    # Use qpylib REST helper method to make a call to QRadar GAF API and return all apps
    result = qpylib.REST('GET', '/api/gui_app_framework/applications')

    if result.status_code != 200:
        return jsonify("QRadar returned {0} ({1})"
                       .format(str(result.status_code), json.dumps(result.json()["message"]))), 500

    # Extract relevant details from response, excluding the app manager app itself
    app_details = [
        (app.get("manifest").get("name", "No Name"),
         app.get("application_state").get("application_id", "No ID"),
         app.get("manifest").get("version", "No Version"),
         app.get("application_state").get("status", "No Status"),
         app.get("manifest").get("uuid", "No UUID")) for app in result.json() if
        app.get("manifest").get("uuid") != OWN_UUID]

    return jsonify(app_details)


# Check request method and adjust app status/delete app accordingly, extracting app id as url parameter
@app.route('/apps/<app_id>', methods=['POST', 'DELETE'])
def manage_app(app_id):
    if request.method == 'POST':
        status = request.args.get('status')
        params = {'status': status}

        result = qpylib.REST('POST', '/api/gui_app_framework/applications/%s' % app_id, params=params)

        if result.status_code != 200:
            return jsonify("QRadar returned {0} ({1})"
                           .format(str(result.status_code), json.dumps(result.json()["message"]))), 500

        return jsonify("App status set to %s" % status), 200

    elif request.method == 'DELETE':
        result = qpylib.REST('DELETE', '/api/gui_app_framework/applications/%s' % app_id)

        if result.status_code != 204:
            return jsonify("QRadar returned {0} ({1})"
                           .format(str(result.status_code), json.dumps(result.json()["message"]))), 500

        return jsonify("App " + app_id + " deleted"), 200
