"""
Licensed Materials - Property of IBM
5725I71-CC011829
(C) Copyright IBM Corp. 2017, 2018. All Rights Reserved.
US Government Users Restricted Rights - Use, duplication or
disclosure restricted by GSA ADP Schedule Contract with IBM Corp.

This file defines two endpoints that the sample app uses '/index' and
'/getcontext'. Index provides the Right Click Sample app main page while
GetContext provides a JSON object with the app ID and IP selected by the
right click.
"""

__author__ = 'IBM'

from app import app
from flask import jsonify, request, render_template
import json
from qpylib import qpylib


@app.route('/')
@app.route('/index')
def index():
    """
    Index populates a Jinja template with the IP address supplied in the
    query parameter, returning a page displaying the IP
    """
    # Get the IP address provided by query parameter
    ip = request.args.get("ip")
    # If the IP address isn't provided, set the ip to an empty string
    if ip is None:
        ip = ""
    # Display the IP address by rendering the template 'index.html'
    return render_template("index.html", ip=ip)


@app.route('/getcontext', methods=['GET'])
def get_context():
    """
    GetContext gets the app ID and IP and returns a JSON object with
    both bundled into it
    """
    # Get the context provided by the REST call
    context = request.args.get("context")
    # Return the app ID and the IP address
    return json.dumps({"app_id": qpylib.get_app_id(), "ip": context})
