/**
 * Licensed Materials - Property of IBM
 * 5725I71-CC011829
 * (C) Copyright IBM Corp. 2017, 2018. All Rights Reserved.
 * US Government Users Restricted Rights - Use, duplication or
 * disclosure restricted by GSA ADP Schedule Contract with IBM Corp.
 */

/**
 * Renders the column content, parsed from the JSON data output by the REST call
 * @param {*} jsonTagId The ID of the div that contains the raw JSON output of the REST call
 * @param {*} targetDivTagId The ID of the div to output the custom column content to
 */
function renderJsonContent(jsonTagId, targetDivTagId) {
	// Gets the JSON Content that is returned by the REST call
	// This JSON content is stored in a script tag with the
	// ID contained in the variable jsonTagId that is passed
	// to this function
	// Get the JSON content from this tag
	var jsonTagContent = $("#" + jsonTagId).html();
	// Parse the JSON content into a JSON object
	var json = JSON.parse(jsonTagContent);
	// The custom column cell ID is passed through as targetDivTagId
	// Populate the custom column cell with the custom data
	$("#" + targetDivTagId).html("ID" + json.data.id + ";" + " IP" + json.data.offense_source);
}