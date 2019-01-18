"""Licensed Materials - Property of IBM
5725I71-CC011829
(C) Copyright IBM Corp. 2017, 2018. All Rights Reserved.
US Government Users Restricted Rights - Use, duplication or
disclosure restricted by GSA ADP Schedule Contract with IBM Corp."""
"""
QRadar app to make requests to the QRadar Ariel API, retrieving data about events
and flows
API information such as parameters and response details can be found in the QRadar
API documentation
A list of endpoints can be retrived by calling /api/help/endpoints in QRadar
"""
__author__ = 'IBM'

import time
import json

from app import app, qpylib, render_template, request

# API endpoint for Ariel Database searches
ARIEL_SEARCHES_ENDPOINT = '/api/ariel/searches'
# Timeout to wait until giving up on polling an Ariel search
TIMEOUT_MILLISECONDS = 15000
# JSON headers for all requests
JSON_HEADERS = {'content-type': 'application/json'}

# Response when a request with no response body is successful
SUCCESS_RESPONSE = {'success': 'true'}
# Response when a request with no response body fails
FAILURE_RESPONSE = {'success': 'false'}
# Response when a polling request times out
TIMEOUT_RESPONSE = {'error': 'Query timed out'}


@app.route('/')
@app.route('/index')
def index():
    """
    Index page, return HTML page with JavaScript embedded calling the
    different endpoints when submitted
    """
    return render_template('index.html')


@app.route('/delete')
def delete():
    """
    Delete an Ariel search, removing it's results
    """
    # Get the search ID from the request to this endpoint
    # /delete?search_id=SEARCH_ID
    search_id = request.args.get('search_id')
    # Make an HTTP DELETE request to the Ariel searches endpoint specifying
    # a search to delete
    # /api/ariel/searches/SEARCH_ID
    response = qpylib.REST(
        'DELETE',
        '{0}/{1}'.format(ARIEL_SEARCHES_ENDPOINT, search_id),
        headers=JSON_HEADERS
    )
    if response.ok:
        # If the response is HTTP 200 OK
        # The request has been successful
        return json.dumps(SUCCESS_RESPONSE)
    # Otherwise the request has failed
    return json.dumps(FAILURE_RESPONSE)


@app.route('/cancel')
def cancel():
    """
    Mark an Ariel search as canceled, stopping it from processing further but retaining it's
    results
    """
    # Get search ID
    search_id = request.args.get('search_id')
    # Parameter of ?status=CANCELED
    params = {'status': 'CANCELED'}
    # Make an HTTP POST request to the Ariel searches endpoint specifying
    # a search to update the status of to 'CANCELED'
    # /api/ariel/searches/SEARCH_ID?status=CANCELED
    response = qpylib.REST(
        'POST',
        '{0}/{1}'.format(ARIEL_SEARCHES_ENDPOINT, search_id),
        headers=JSON_HEADERS,
        params=params
    )
    if response.ok:
        # Successful request
        return json.dumps(SUCCESS_RESPONSE)
    # Failed request
    return json.dumps(FAILURE_RESPONSE)


@app.route('/save_results')
def save_results():
    """
    Update an Ariel search to ensure that it's results are saved
    """
    # Get search ID
    search_id = request.args.get('search_id')
    # Parameter of ?save_results=true
    params = {'save_results': 'true'}
    # Make an HTTP POST request to the Ariel searches endpoint specifying
    # a search to update to have the results of of it's search saved
    # /api/ariel/searches/SEARCH_ID?save_results=true
    response = qpylib.REST(
        'POST',
        '{0}/{1}'.format(ARIEL_SEARCHES_ENDPOINT, search_id),
        headers=JSON_HEADERS,
        params=params
    )
    if response.ok:
        # Successful request
        return json.dumps(SUCCESS_RESPONSE)
    # Failed request
    return json.dumps(FAILURE_RESPONSE)


@app.route('/poll')
def poll():
    """
    Repeatedly call the Ariel API to check if a search has finished processing
    if it has, retrieve and return the results
    Poll only as long as the timeout defined
    """
    # Get search ID
    search_id = request.args.get('search_id')
    # Start time that the polling began at
    init_time = time.time()
    while init_time + TIMEOUT_MILLISECONDS > time.time():
        # While within the timeout
        # Poll with an HTTP GET request to the Ariel searches endpoint specifying
        # a search to retrieve the information of
        # /api/ariel/searches/SEARCH_ID
        response = qpylib.REST(
            'GET',
            '{0}/{1}'.format(ARIEL_SEARCHES_ENDPOINT, search_id),
            headers=JSON_HEADERS
        ).json()
        if 'http_response' in response:
            # If there's an 'http_response' attribute in the response
            # the request has failed, output the response and error
            return json.dumps(response)
        if response['status'] == 'COMPLETED':
            # If the status of the query is COMPLETED, the results can now be retrieved
            # Make an HTTP GET request to the Ariel searches endpoint specifying
            # a search to retrieve the results of
            # /api/ariel/searches/SEARCH_ID/results
            response = qpylib.REST(
                'GET',
                '{0}/{1}/results'.format(ARIEL_SEARCHES_ENDPOINT, search_id),
                headers=JSON_HEADERS
            ).json()
            # Return the results
            return json.dumps(response)
        # Wait for 1 second before polling again to avoid spamming the API
        time.sleep(1)
    # If the polling has timed out, return an error
    return json.dumps(TIMEOUT_RESPONSE)


@app.route('/progress')
def progress():
    """
    Gets information about a search and returns details on the search status and progress
    of execution
    """
    # Get search ID
    search_id = request.args.get('search_id')
    # HTTP GET to /api/ariel/searches/SEARCH_ID
    response = qpylib.REST(
        'GET',
        '{0}/{1}'.format(ARIEL_SEARCHES_ENDPOINT, search_id),
        headers=JSON_HEADERS
    ).json()
    if 'http_response' in response:
        # Request failed
        return json.dumps(response)
    # Request successful
    # Parse the response from the API for status and progress and
    # return them as a new JSON object
    return json.dumps(
        {
            'status': str(response['status']),
            'progress': str(response['progress'])
        }
    )


@app.route('/results')
def results():
    """
    Retrieves the results of a search
    """
    # Get search ID
    search_id = request.args.get('search_id')
    # HTTP GET to /api/ariel/searches/SEARCH_ID/results
    response = qpylib.REST(
        'GET',
        '{0}/{1}/results'.format(ARIEL_SEARCHES_ENDPOINT, search_id),
        headers=JSON_HEADERS
    ).json()
    # Return the response
    return json.dumps(response)


@app.route('/search')
def search():
    """
    Creates a new search with the query provided, returns a search ID to allow further
    search interaction, such as retrieving results
    """
    # Get search ID
    query = request.args.get('query')
    # Parameter of ?query_expression=QUERY
    params = {'query_expression': query}
    # HTTP POST to /api/ariel/searches?query_expression=QUERY
    response = qpylib.REST(
        'POST',
        ARIEL_SEARCHES_ENDPOINT,
        headers=JSON_HEADERS,
        params=params
    ).json()
    # Return the response
    return json.dumps(response)


@app.route('/searches')
def searches():
    """
    Lists existing searchs on the Ariel DB, including ones that have completed execution
    """
    # HTTP GET to /api/ariel/searches
    response = qpylib.REST(
        'GET',
        ARIEL_SEARCHES_ENDPOINT,
        headers=JSON_HEADERS
    ).json()
    # Return the response
    return json.dumps(response)


@app.route('/search_info')
def search_info():
    """
    Gets information about a search, such as status, progress and other meta data
    """
    # Get search ID
    search_id = request.args.get('search_id')
    # HTTP GET to /api/ariel/searches/SEARCH_ID
    response = qpylib.REST(
        'GET',
        '{0}/{1}'.format(ARIEL_SEARCHES_ENDPOINT, search_id),
        headers=JSON_HEADERS
    ).json()
    # Return the response
    return json.dumps(response)
