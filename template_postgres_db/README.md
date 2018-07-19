# PostgreSQL Database Sample App
## Overview
This sample app provides an example of how to host a PostgreSQL Database in a QRadar app.  
The app sets up a simple database with a table *fruit* which is queried and inserted into.
## Setup
The app is set up with a database with a user *postgres* that can access it.  
NOTE - the user *postgres* is set up as **trust** in **/store/data/pg_hba.conf** meaning that there is no password authentication on connecting to the database as this user.
## Files
### views.py
The initial database set up; creating the table and inserting some starting rows, is in the views.py file and executed when the app is started.  
The endpoints for this app are defined in *views.py*.  
The endpoint **/index** returns a template populated with data retrieved from the database.  
The endpoint **/add_fruit** takes a query parameter *fruit* and uses that as a name to insert a new row into the 'fruit' table.  
### manifest.json
The *manifest.json* file simply defines properties for this app, such as name and description.
### postgres-setup.sh
The *postgres-setup.sh* file found in **/src_deps/init/** installs PostgreSQL and Psycopg2 and configures the database.
### init/ordering.txt
The *ordering.txt* file found in **/src_deps/init/** simply starts the *postgres-setup.sh* script.
## Dependencies
The dependencies for this app are retrieved using yum, and as such **requires an internet connection**.
### PostgreSQL
The four PostgreSQL dependencies that are installed are:
**lib -> postgres -> server -> devel**.
### Psycopg2
Psycopg2 is installed and is a driver that allows Python to interact with the PostgreSQL Database.
