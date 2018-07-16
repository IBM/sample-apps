"""
Licensed Materials - Property of IBM
5725I71-CC011829
(C) Copyright IBM Corp. 2017, 2018. All Rights Reserved.
US Government Users Restricted Rights - Use, duplication or
disclosure restricted by GSA ADP Schedule Contract with IBM Corp.

This sample app shows how environmental variables defined in the manifest can be retrieved by the app.
This file defines the endpoint /index that returns a message with the retrieved environmental
variable appended to it
"""
import platform

__author__ = 'IBM'

from app import app, qpylib
import os

# Environemntal Variable name
variable_name = "CUSTOM_ENVIRONMENTAL_VARIABLE"
 
@app.route('/')
@app.route('/index')
def index():
    """
    Returns a message with the environmental variable 'CUSTOM_ENVIRONMENTAL_VARIABLE' appended
    to it
    """
    # Return a message with the environmental variable retrieved appended to it
    return "Message retrieved from environmental variable: " + os.environ.get(variable_name, None)
