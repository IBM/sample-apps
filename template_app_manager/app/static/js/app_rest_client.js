/*
Licensed Materials - Property of IBM
5725I71-CC011829
(C) Copyright IBM Corp. 2017, 2018. All Rights Reserved.
US Government Users Restricted Rights - Use, duplication or
disclosure restricted by GSA ADP Schedule Contract with IBM Corp.
*/

/**
JS File containing functions to encapsulate app REST API calls
**/
var appsEndpoint = 'apps';

/**
GET /apps function
**/
function getApps( )
{
  var getAppsDeferred = $.Deferred();
  var ajax = $.ajax({
    type : "GET",
    url : appsEndpoint,
    contentType : "application/json"
  }).always( function ()
  {
    getAppsDeferred.resolve( ajax );
  });
  return getAppsDeferred;
}

/**
POST /apps/application_id function
**/
function startStopApp( app_id, status )
{
  var params = $.param( { 'status' : status } );
  var endpoint = appsEndpoint + '/' + app_id + '?' + params;

  var startStopAppDeferred = $.Deferred();
  var ajax = $.ajax({
    type : "POST",
    url : endpoint,
    contentType : "application/json"
  }).always( function ()
  {
    startStopAppDeferred.resolve( ajax );
  });
  return startStopAppDeferred;
}

/**
DELETE /apps/application_id function
**/
function deleteApp( app_id )
{
  var endpoint = appsEndpoint + '/' + app_id;

  var deleteDeferred = $.Deferred();
  var ajax = $.ajax({
    type : "DELETE",
    url : endpoint,
    contentType : "application/json"
  }).always( function ()
  {
    deleteDeferred.resolve( ajax );
  });
  return deleteDeferred;
}