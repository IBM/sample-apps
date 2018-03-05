"""Licensed Materials - Property of IBM
5725I71-CC011829
(C) Copyright IBM Corp. 2017, 2018. All Rights Reserved.
US Government Users Restricted Rights - Use, duplication or
disclosure restricted by GSA ADP Schedule Contract with IBM Corp."""
__author__ = 'IBM'



from app import app
from qpylib import qpylib
import json

@app.route('/offenseListFunction', methods=['GET'])
def offense_list_function():
    qpylib.log("offense_list_function", "info")

    #You can process the data and return any value here, that will be passed into javascript
    return json.dumps({'custom_data_from_python_view': "your_content_here"})
