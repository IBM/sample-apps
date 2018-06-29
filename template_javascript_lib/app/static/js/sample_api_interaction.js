/**
Licensed Materials - Property of IBM
5725I71-CC011829
(C) Copyright IBM Corp. 2017, 2018. All Rights Reserved.
US Government Users Restricted Rights - Use, duplication or
disclosure restricted by GSA ADP Schedule Contract with IBM Corp.

Sample JavaScript class that utilises the standard QRadar JavaScript
library to do various functions.

All outputs of this class are to a DOM element with the ID 'output'
*/

/**
 * Outputs a list of offenses in the system in JSON form.
 * Offense data is retrieved from the API /api/siem/offenses
 * Uses QRadar.rest()
 */
function listOffenses() {
    // Make an HTTP GET request to /api/siem/offenses
    QRadar.rest(
        {
            path: '/api/siem/offenses',
            httpMethod: 'GET',
            onComplete: function () {
                // When the request is complete, the response is accessible through this.response
                // Output the response to the output div in prettified JSON form
                document.getElementById('output').innerHTML = JSON.stringify(this.response, null, 4);
            }
        }
    );
}

/**
 * Outputs a specific offense, identified by the offense ID 
 * provided, in JSON form.
 * Offense data is retrieved from the API /api/siem/offenses/OFFENSE_ID
 * Uses QRadar.rest()
 * @param {*} offenseID the ID of the offense
 */
function getOffense(offenseID) {
    // Make an HTTP GET request to /api/siem/offenses/OFFENSE_ID
    QRadar.rest(
        {
            path: '/api/siem/offenses/' + offenseID,
            httpMethod: 'GET',
            onComplete: function () {
                // When the request is complete, the response is accessible through this.response
                // Output the response to the output div in prettified JSON form
                document.getElementById('output').innerHTML = JSON.stringify(this.response, null, 4);
            }
        }
    );
}

/**
 * Outputs the current user that is currently logged in, with details such as name and role
 * Uses QRadar.getCurrentUser()
 */
function getCurrentUser() {
    // Output the current user, retrieved through QR
    document.getElementById('output').innerHTML = JSON.stringify(QRadar.getCurrentUser(), null, 4);
}

/**
 * Opens the offense specified by the ID provided within QRadar in the offenses tab
 * @param {*} offenseID the offense ID to open
 * Uses QRadar.openOffense(id, windowOpen)
 */
function openOffenseTab(offenseID) {
    QRadar.openOffense(offenseID, false);
}

/**
 * Opens the offense specified by the ID provided in a new window
 * @param {*} offenseID the offense ID to open
 * Uses QRadar.openOffenseWindow(id, windowOpen)
 */
function openOffenseWindow(offenseID) {
    QRadar.openOffense(offenseID, true);
}

/**
 * Outputs a cookie from the browser, specified by the cookie name
 * Note, cookies with HTTPOnly flag cannot be accessed through JavaScript
 * Uses QRadar.getCookie(cookieName)
 * @param {*} name the name of the cookie to retrieve
 */
function getCookie(name) {
    document.getElementById('output').innerHTML = QRadar.getCookie(name);
}

/**
 * Outputs the full path of a REST endpoint provided
 * Builds the full URL based on if '/api/', '/application/' or a full URL is provided
 * Uses QRadar.buildRestUrl(endpoint)
 * @param {*} endpoint the endpoint to build the path from
 */
function getFullRESTPath(endpoint) {
    document.getElementById('output').innerHTML = QRadar.buildRestUrl(endpoint);
}

/**
 * Runs an AQL query within QRadar opening the results within the events tab
 * Uses QRadar.openEventSearch(query, windowOpen)
 * @param {*} query the AQL query to execute
 */
function runAQLEventTab(query) {
    // Param of windowOpen=false means open in tab
    QRadar.openEventSearch(query, false);
}

/**
 * Runs an AQL query opening the results in a new window in viewer
 * Uses QRadar.openEventSearch(query, windowOpen)
 * @param {*} query the AQL query to execute
 */
function runAQLEventWindow(query) {
    // Param of windowOpen=true means open in new window
    QRadar.openEventSearch(query, true);
}

/**
 * Runs an AQL query within QRadar opening the results within the flows tab
 * Uses QRadar.openFlowSearch(query, windowOpen)
 * @param {*} query the AQL query to execute
 */
function runAQLFlowTab(query) {
    // Param of windowOpen=false means open in tab
    QRadar.openFlowSearch(query, false);
}

/**
 * Runs an AQL query opening hte reuslts in a new window in viewer
 * Uses QRadar.openFlowSearch(query, windowOpen)
 * @param {*} query the AQL query to execute
 */
function runAQLFlowWindow(query) {
    // Param of windowOpen=true means open in new window
    QRadar.openFlowSearch(query, true);
}

/**
 * Opens an asset specified by the ID provided within QRadar in the assets tab
 * Uses QRadar.openAsset(assetID, windowOpen)
 * @param {*} assetID the ID of the asset to open
 */
function openAssetTabByID(assetID) {
    // Param of windowOpen=false means open in tab
    QRadar.openAsset(assetID, false)
}

/**
 * Opens an asset specified by the ID provided in a new window in viewer
 * Uses QRadar.openAsset(assetID, windowOpen)
 * @param {*} assetID the ID of the asset to open
 */
function openAssetWindowByID(assetID) {
    // Param of windowOpen=true means open in new window
    QRadar.openAsset(assetID, true)
}

/**
 * Outputs a list of named services in the system in JSON form.
 * Named service data is retrieved from /api/gui_app_framework/named_services
 * Uses QRadar.rest()
 */
function getNamedServices() {
    // Make an HTTP GET request to /api/gui_app_framework/named_services
    QRadar.rest(
        {
            path: '/api/gui_app_framework/named_services',
            httpMethod: 'GET',
            onComplete: function () {
                // When the request is complete, the response is accessible through this.response
                // Output the response to the output div in prettified JSON form
                document.getElementById('output').innerHTML = JSON.stringify(this.response, null, 4);
            }
        }
    );
}