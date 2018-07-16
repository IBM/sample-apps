# Right Click Sample App
## Overview
This sample app provides an example of including right click functionality within an app.  
When you go to the Log Activity tab and right click on an IP address in the event viewer a right click menu is brought up; in this right click menu under 'More Options...' there is the choice to 'Get IP info in sample app' - when you press this it opens the right click sample app with the IP information you selected.
## Files
### manifest.json
The *manifest.json* file defines a number of app properties.  
* The app details such as name and version.
* The GUI action, defining the JavaScript function to call when the right click event is triggered, alongside a REST method to call.
* The page scripts to be loaded on the EventList page, the custom right click JS file and the standard qappfw JS file
* The app area index page that displays the IP address passed to it
### right_click.js
The *right_click.js* file defines the right click function that is called whenever the GUI action is triggered.  
The function opens a new window for the right click sample app and supplies the IP to display to it.
### views.py
The *views.py* file defines the HTTP endpoints for the Flask server.  
* Index populates a Jinja template with the IP address supplied in the query parameter, returning a page displaying the IP.
* GetContext gets the app ID and IP and returns a JSON object with both bundled into it.
### index.html
The *index.html* file is a template that simply injects the IP address provided into the page.