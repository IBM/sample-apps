# Environmental Variables Sample App
## Overview
This sample app shows how environmental variables defined in the manifest can be retrieved by the app.
## Files
### manifest.json
The *manifest.json* file defines the app details such as name and version, and also defines the environmental variable that is going to be retrieved.
### views.py
The *views.py* file defines the HTTP endpoints for the app, with **/index** being the only one.  
The **/index** endpoint simply returns the message retrieved from the environemental variable in the manifest.