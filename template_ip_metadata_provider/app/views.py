"""Licensed Materials - Property of IBM
5725I71-CC011829
(C) Copyright IBM Corp. 2017, 2018. All Rights Reserved.
US Government Users Restricted Rights - Use, duplication or
disclosure restricted by GSA ADP Schedule Contract with IBM Corp."""
__author__ = 'IBM'



from app import app
from flask import render_template
from flask import request
from qpylib import qpylib

import json

@app.route('/ip_metadata_provider', methods=['GET'])
def getIPMetadata():
    app_id = qpylib.get_app_id()
    context = request.args.get('context')

    metadata_dict = {
        'key': 'exampleIPMetadataProvider',
        'label': 'Extra metadata:',
        'value': 'Metadata value',
        'html': render_template('metadata_ip.html', ip_address=context, app_id=app_id)
    }

    return json.dumps(metadata_dict)
