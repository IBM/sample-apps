# Licensed Materials - Property of IBM
# 5725I71-CC011829
# (C) Copyright IBM Corp. 2017, 2018. All Rights Reserved.
# US Government Users Restricted Rights - Use, duplication or
# disclosure restricted by GSA ADP Schedule Contract with IBM Corp.

if [ ! -f /store/flyway_exists.txt ]; then
    # If Flyway hasn't been set up yet
    # Move the Flyway tar package to the store directory
    mv /src_deps/init/flyway.tar.gz /store/flyway.tar.gz
    # Move into store
    cd /store
    # Extract Flyway
    tar -xf flyway.tar.gz
    # Remove the Flyway tar pac kage
    rm flyway.tar.gz
    # Move out of store
    cd ..
    # Create a marker file to show that Flyway has been set up
    touch /store/flyway_exists.txt
else
    # If Flyway has already been created, delete the Flyway tar
    rm /src_deps/init/flyway.tar.gz
fi