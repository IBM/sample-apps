"""Licensed Materials - Property of IBM
5725I71-CC011829
(C) Copyright IBM Corp. 2017, 2018. All Rights Reserved.
US Government Users Restricted Rights - Use, duplication or
disclosure restricted by GSA ADP Schedule Contract with IBM Corp."""
__author__ = 'IBM'


from flask import render_template
from app import app

@app.route('/admin_screen')
def admin_screen():
    return render_template("admin_screen.html")
