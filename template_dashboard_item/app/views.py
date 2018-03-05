"""Licensed Materials - Property of IBM
5725I71-CC011829
(C) Copyright IBM Corp. 2017, 2018. All Rights Reserved.
US Government Users Restricted Rights - Use, duplication or
disclosure restricted by GSA ADP Schedule Contract with IBM Corp."""
__author__ = 'IBM'



import json

from flask import render_template
from qpylib import qpylib
from app import app


#build a Flask app route, this route will build a Json construct, of which there is a 'html' attribute to contain a html string
@app.route('/getExampleDashboardItem', methods=['GET'])
def getExampleDashboardItem():
    try:
        qpylib.log("getExampleDashboardItem>>>")
        return json.dumps({'id':'ExampleDashBoardItem','title':'Example Dashboard','HTML':render_template('dashboard.html') })
    except Exception as e:
        qpylib.log( "Error "  + str(e) )
        raise
