"""
Licensed Materials - Property of IBM
5725I71-CC011829
(C) Copyright IBM Corp. 2017, 2018. All Rights Reserved.
US Government Users Restricted Rights - Use, duplication or
disclosure restricted by GSA ADP Schedule Contract with IBM Corp.

This file defines the endpoints for the app: '/'index and '/'.
When these endpoints are called they return index.html in
the static folder
"""

__author__ = 'IBM'

from app import app, render_template

@app.route('/')
@app.route('/index')
def index():
    """
    Index endpoint - returns index.html when called
    """
    # Return templates/index.html
    return render_template('index.html')
