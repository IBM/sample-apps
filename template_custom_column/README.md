# Custom Column App
## Overview
This sample app shows how to add a custom column to the offense tab.  
The custom column works by calling the *custom_column_method* with the ID of each offense row; this endpoint takes an offense ID and then returns offense data from the QRadar REST API for it.  
This returned offense data is fed into *renderJsonContent* in *custom_offense.js*, which parses the data and outputs the formatted data into the custom column div.
## Files
### manifest.json
The *manifest.json* file defines app properties such as name and version.  
The manifest also defines the endpoint *custom_column_method* for QRadar to call for the custom column and the JavaScript page script *custom_offense.js* to use on the OffenseList page.
### views.py
The *views.py* file defines the endpoint that the app uses *custom_column_method*.
### custom_offense.js
The *custom_offense.js* file defines the function *renderJsonContent* which takes the raw offense JSON data and outputs it to the custom column div.