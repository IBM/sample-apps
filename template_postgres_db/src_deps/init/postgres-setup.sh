# Licensed Materials - Property of IBM
# 5725I71-CC011829
# (C) Copyright IBM Corp. 2017, 2018. All Rights Reserved.
# US Government Users Restricted Rights - Use, duplication or
# disclosure restricted by GSA ADP Schedule Contract with IBM Corp.

# Install dependencies
# NOTE - must be done in this order lib -> postgres -> server -> devel
rpm -ivh /src_deps/init/postgresql96-libs-9.6.9-1PGDG.rhel6.x86_64.rpm
rpm -ivh /src_deps/init/postgresql96-9.6.9-1PGDG.rhel6.x86_64.rpm
rpm -ivh /src_deps/init/postgresql96-server-9.6.9-1PGDG.rhel6.x86_64.rpm
rpm -ivh /src_deps/init/postgresql96-devel-9.6.9-1PGDG.rhel6.x86_64.rpm

if [ ! -f /store/db_exists.txt ]; then
    # If the database hasn't been created yet - i.e. first install not upgrade
    # Create the new data directory to store the database info in
    mkdir /store/data
    # Assign the new data directory ownership to the postgres user
    chown postgres /store/data
    # Initialise the database cluster to the data directory
    su - postgres -c "/usr/pgsql-9.6/bin/pg_ctl -D /store/data initdb"
    # Put down a marker file to show the database exists for future upgrades
    touch /store/db_exists.txt
fi

# Start the database, output logs to /store/data/postgres.log
su - postgres -c "/usr/pgsql-9.6/bin/pg_ctl -D /store/data -l /store/data/postgres.log start"