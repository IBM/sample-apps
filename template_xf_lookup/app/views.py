"""Licensed Materials - Property of IBM
5725I71-CC011829
(C) Copyright IBM Corp. 2017, 2018. All Rights Reserved.
US Government Users Restricted Rights - Use, duplication or
disclosure restricted by GSA ADP Schedule Contract with IBM Corp."""
__author__ = 'IBM'


from app import app
from flask import render_template, jsonify
from qpylib import qpylib
import requests

# Fill in your X-force API details here
API_KEY = ''
API_PASS = ''
OFFENSES_API_VERSION = '7.0'


@app.route('/offenseHeader/<offense_id>', methods=['GET'])
def offenseHeader(offense_id):
    headers = {'content_type': 'application/json', 'Version':OFFENSES_API_VERSION}
    params = {'fields': 'offense_source'}
    restReturn = qpylib.REST('GET', 'api/siem/offenses/' + str(offense_id), headers=headers, params=params)
    lastrep = None
    offenseSource = None
    cats = None

    try:
        if restReturn.status_code == 200:
            restReturnJson = restReturn.json()
            qpylib.log('Offenses API returned: %s' % restReturnJson, level='debug')
            offenseSource = restReturnJson['offense_source']
            xResponse = requests.get('https://api.xforce.ibmcloud.com/ipr/history/' + offenseSource, auth=(API_KEY,API_PASS))
            if xResponse.status_code == 200:
                xJson = xResponse.json()
                qpylib.log('Xforce API returned: %s' % xJson, level='debug')
                history = xJson.get("history")
                lastrep = history[-1]
                cats = lastrep.get("cats").keys()
        html = render_template('xforce_details.html', ip=offenseSource, rep=lastrep, cats=cats)
        return jsonify({'html': html})
    except Exception as e:
        html = render_template('xforce_details.html', ip=offenseSource, rep=lastrep, cats=cats, error=str(e))
        return jsonify({'html': html})
