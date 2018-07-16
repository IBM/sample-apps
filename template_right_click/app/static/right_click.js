// Licensed Materials - Property of IBM
// 5725I71-CC011829
// (C) Copyright IBM Corp. 2017, 2018. All Rights Reserved.
// US Government Users Restricted Rights - Use, duplication or
// disclosure restricted by GSA ADP Schedule Contract with IBM Corp.
/**
 * Function to be executed on right click of an IP address in the event viewer, 
 * opens the IP address right clicked in the right click sample app
 * @param {*} result contextual result from the REST, containing app ID and IP address right clicked
 */
function right_click(result) {
	// Initialise app ID and IP address
	var app_id = ""
	var ip_addr = ""

	
	if (result) {
		// If the result passed through isn't null/undefined/empty
		// Assign out the app ID and IP address
		app_id = encodeURI(result.app_id)
		ip_addr = encodeURI(result.ip)
	}

	if(app_id && ip_addr)
	{
		// If the app ID and IP address aren't null/undefined/empty
		// Open the right click sample app in a new window
		QRadar.windowOrTab("plugins/" + app_id + "/app_proxy/index?ip=" + ip_addr);
	}
}