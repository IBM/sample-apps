"""
Licensed Materials - Property of IBM
5725I71-CC011829
(C) Copyright IBM Corp. 2017, 2018. All Rights Reserved.
US Government Users Restricted Rights - Use, duplication or
disclosure restricted by GSA ADP Schedule Contract with IBM Corp.

QRadar Sample app showing how to host a PostgreSQL database in an app.
"""
__author__ = "IBM"

# Import JSON and psycopg2 PostgreSQL driver
import json
import psycopg2
from app import app, render_template, request
# Use RealDictCursor for retrieving dict objects from requests
from psycopg2.extras import RealDictCursor

# This is run when the app is started
# Database interaction details
DATABASE_NAME = "postgres"
POSTGRES_USER = "postgres"
# Connect to the database
conn = psycopg2.connect(
    "dbname={0} user={1}"
    .format(DATABASE_NAME, POSTGRES_USER))
# Open a database cursor
cur = conn.cursor()
# Execute a command checking if the table 'fruit' exists
cur.execute("SELECT EXISTS(SELECT * FROM information_schema.tables WHERE table_name=%s)", ("fruit",))
if cur.fetchone()[0] == False:
    # If 'fruit' doesn't exist
    # Create fruit table
    cur.execute("CREATE TABLE fruit (id serial PRIMARY KEY, name varchar);")
    # Add 3 fruit entries
    cur.execute("INSERT INTO fruit (name) VALUES ('Apple'), ('Orange'), ('Banana');")
    # Commit changes
    conn.commit()
# Close cursor and DB connection
cur.close()
conn.close()

 
@app.route("/")
@app.route("/index")
def index():
    """
    Base endpoint, returning a template that is populated with the
    data stored in the PostgreSQL DB Table 'fruit'
    """
    try:
        # Open connection to DB
        conn = psycopg2.connect(
            "dbname={0} user={1}"
            .format(DATABASE_NAME, POSTGRES_USER))
        # Open a database cursor
        # This cursor uses 'RealDictCursor' which just means the results are in
        # Python dictionary form rather than the default tuples
        # This allows for easier parsing into JSON
        cur = conn.cursor(cursor_factory=RealDictCursor)
        # Execute a select command
        cur.execute("SELECT * FROM fruit;")
        # Get the results of the command
        results = cur.fetchall()
        # Close the cursor and DB connection
        cur.close()
        conn.close()
        # Parse the results into JSON and feed them into the Jinja template
        return render_template("index.html", fruits=json.loads(json.dumps(results)))
    except Exception as e:
        # If there is an exception, return the exception string
        return str(e)

@app.route("/add_fruit")
def addFruit():
    """
    Endpoint to add a new fruit to the PostgreSQL DB table 'fruit'
    Fruit name is passed as a query parameter, and the ID is generated
    through autoincrementation in the DB
    """
    try:
        # Get the '?fruit=FRUIT' query parameter value passed to this endpoint
        fruit = request.args.get("fruit")
        # Open a database connection
        conn = psycopg2.connect(
            "dbname={0} user={1}"
            .format(DATABASE_NAME, POSTGRES_USER))
        # Open a database cursor
        cur = conn.cursor()
        # Execute an insert command
        # NOTE - this uses psycopg method for inserting values into a DB query
        # You should not manually concatenate
        cur.execute("INSERT INTO fruit (name) VALUES (%s)", [fruit])
        # Commit the changes to the DB
        conn.commit()
        # Close the cursor and DB connection
        cur.close()
        conn.close()
        # Return successful request
        return json.dumps({"success":True})
    except Exception as e:
        # If there is an exception, return the exception string
        return str(e)
