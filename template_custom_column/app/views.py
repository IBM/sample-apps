"""
Licensed Materials - Property of IBM
5725I71-CC011829
(C) Copyright IBM Corp. 2017, 2018. All Rights Reserved.
US Government Users Restricted Rights - Use, duplication or
disclosure restricted by GSA ADP Schedule Contract with IBM Corp.

This file contains the '/custom_column_method/<offense_id>' REST
endpoint, this endpoint simply returns offense data retrieved
from the QRadar REST API with the ID provided. This data can
then be used to populate a custom column in the offense tab.
"""

__author__ = 'IBM'

from flask import Response
from app import app
from qpylib.qpylib import log
from qpylib.offense_qpylib import get_offense_json_ld
import json

@app.route('/custom_column_method/<offense_id>', methods=['GET'])
def get_offense(offense_id):
    """
    This endpoint takes an offense ID and uses it to retrieve offense
    data about the matching offense using the QRadar REST API
    """
    # Use the qpylib function get_offense_json_ld to get offense data
    # by offense ID in JSON form
    offense_json = get_offense_json_ld(offense_id)
    # Return the offense JSON
    return Response(response=offense_json, status=200, mimetype='application/json')
