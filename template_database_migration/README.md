# Flyway Database Migration Sample App
## Overview
This sample app provides an example of using Flyway database migration management with PostgreSQL to manage database versions and migrate between them.  
This sample creates a database with a table *fruit*, inserts data into it and adds a new column *color* and populates it with some data.
## Setup
The app is set up with a database with a user *postgres* that can access it.  
NOTE - the user *postgres* is set up as **trust** in **/store/data/pg_hba.conf** meaning that there is no password authentication on connecting to the database as this user.  
The software *Flyway* is installed in this app, and it's configuration file is within the tar package in **/flyway-5.1.4/conf/flyway.conf**. This configuration file allows you to configure the database to connect to, the user details and more.
## Files
### views.py
The endpoints for this app are defined in *views.py*.  
The endpoint **/index** returns a template populated with data retrieved from the database.  
The endpoint **/add_fruit** takes a query parameter *fruit* and uses that as a name to insert a new row into the 'fruit' table.  
### manifest.json
The *manifest.json* file simply defines properties for this app, such as name and description.
### flyway-setup.sh
The *flyway-setup.sh* file found in **/src_deps/init** installs Flyway.
### flyway-migrate.sh
The *flyway-migrate.sh* file found in **/src_deps/init** runs the Flyway migrate command.
### postgres-setup.sh
The *postgres-setup.sh* file found in **/src_deps/init/** installs PostgreSQL and configures the database.
### init/ordering.txt
The *ordering.txt* file found in **/src_deps/init/** simply starts the *postgres-setup.sh*, *flyway-setup.sh* and *flyway-migrate.sh* scripts.
### pip/ordering.txt
The *ordering.txt* file found in **/src_deps/init/** installs the pip package *psycopg2*.
### V1__Create_Fruit_Table.sql
The *V1__Create_Fruit_Table.sql* file found in the Flyway tar under **/flyway-5.1.4/sql/** creates the sample table *fruit*.
### V2__Insert_Fruit.sql
The *V2__Insert_Fruit.sql* file found in the Flyway tar under **/flyway-5.1.4/sql/** inserts some sample data into the *fruit* table.
### V3__Create_Color_Column.sql
The *V3__Create_Color_Column.sql* file found in the Flyway tar under **/flyway-5.1.4/sql/** adds a new row *color* to the *fruit* table and updates some values to include the *color*.
## Dependencies
### PostgreSQL
The four PostgreSQL RPMs install PostgreSQL, and must be install in the following order:  
**lib -> postgres -> server -> devel**.
### Psycopg2
The Psycopg2 Python package is a database adapter that allows Python to interact with PostgreSQL.
### Flyway
Flyway is software that assists in managing database migrations.