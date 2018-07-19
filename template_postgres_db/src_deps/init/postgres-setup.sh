# Licensed Materials - Property of IBM
# 5725I71-CC011829
# (C) Copyright IBM Corp. 2017, 2018. All Rights Reserved.
# US Government Users Restricted Rights - Use, duplication or
# disclosure restricted by GSA ADP Schedule Contract with IBM Corp.

# Install dependencies
# NOTE - must be done in this order lib -> postgres -> server -> devel
yum -y install postgresql-libs
yum -y install postgresql
yum -y install postgresql-server
yum -y install postgresql-devel

if [ ! -f /store/db_exists.txt ]; then
    # If the database hasn't been created yet - i.e. first install not upgrade
    # Create the new data directory to store the database info in
    mkdir /store/data
    # Assign the new data directory ownership to the postgres user
    chown postgres /store/data
    # Initialise the database cluster to the data directory
    su - postgres -c "initdb -D /store/data"
    # Put down a marker file to show the database exists for future upgrades
    touch /store/db_exists.txt
fi

# Start the database, output logs to /store/data/postgres.log
su - postgres -c "pg_ctl -D /store/data -l /store/data/postgres.log start"

# Install psycopg2
yum -y install python-psycopg2