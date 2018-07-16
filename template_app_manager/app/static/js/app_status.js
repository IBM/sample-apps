/*
Licensed Materials - Property of IBM
5725I71-CC011829
(C) Copyright IBM Corp. 2017, 2018. All Rights Reserved.
US Government Users Restricted Rights - Use, duplication or
disclosure restricted by GSA ADP Schedule Contract with IBM Corp.
*/

$(document).ready(function() {
  var $NoAppsTR = $( '#NoAppsTR' );

  $(".btn-group .btn").click(function() {
    var inputValue = $(this).find("input").val();

    if (inputValue != 'all') {
      var target = $('table tr[data-status="' + inputValue + '"]');
      $("table tbody tr").not(target).hide();
        target.fadeIn();
    } else {
      $("table tbody tr").not( $NoAppsTR ).fadeIn();
    }
    if ( $("table tbody tr:visible").length === 0 ){
      $NoAppsTR.show();
    }
    else {
      $NoAppsTR.hide();
    }
  });

  $("#refreshButton").click(function() {
    getAppDetails();
  });
  // Changing the class of status label to support Bootstrap 4
  var bs = $.fn.tooltip.Constructor.VERSION;
  var str = bs.split(".");
  if (str[0] == 4) {
    $(".label").each(function() {
      var classStr = $(this).attr("class");
      var newClassStr = classStr.replace(/label/g, "badge");
      $(this).removeAttr("class").addClass(newClassStr);
    });
  }

  // Animate select box
  var searchInput = $(".search-box input");
  var inputGroup = $(".search-box .input-group");
  var inputIcon = $(".search-box i");
  var boxWidth = inputGroup.width();
  searchInput.focus(function() {
    inputGroup.animate({
      width: "250",
    });
    $(this).data('placeholder', $(this).attr('placeholder')).attr('placeholder', '');
    inputIcon.data('color', inputIcon.css("color")).css({
      "color": "#ffffff"
    });
  }).blur(function() {
    inputGroup.animate({
      width: boxWidth
    });
    $(this).attr('placeholder', $(this).data('placeholder'));
    inputIcon.css({
      "color": inputIcon.data('color')
    });
  });

  // Filter table rows based on searched term
  $("#search").on("keyup", function() {
      $NoAppsTR.hide();
      var term = $(this).val().toLowerCase().replace(/[\-\[\]\/\{\}\(\)\*\+\?\.\\\^\$\|]/g, "\\$&");
      $("table tbody tr").not( $NoAppsTR ).each(function(){
          $row = $(this);
          var name = $row.find("td:nth-child(2)").text().toLowerCase();
          if( name.search(term ) < 0 ){
              $row.hide();
          } else{
              $row.show();
          }
      });
      if ( $("table tbody tr:visible").length === 0 ){
        $NoAppsTR.show();
      }
  });

  // Generate table from API response
  getAppDetails();
});

function getAppDetails() {
  var appsPromise = getApps();

  appsPromise.then(function(response) {
    if (response.status === 200) {
      generateTableFromAPIResponse(response.responseJSON);
    } else {
      if (response.readyState == 4) {
        // HTTP error (can be checked by XMLHttpRequest.status and XMLHttpRequest.statusText)
        console.log("HTTP error. Server returned: " + response.statusText);
      } else if (response.readyState === 0) {
        // Network error (i.e. connection refused, access denied due to CORS, etc.)
        console.log("Network error. Please check your internet connection.");
      } else {
        // something weird is happening
        console.log("An unknown error occurred.");
      }
    }
  });
}

function generateTableFromAPIResponse( appDetailsJSON )
{
  $( "#appTable tbody tr" ).not( '#NoAppsTR' ).remove();

  if ( appDetailsJSON.length === 0 )
  {
    // Display no app_status
    $( '#NoAppsTR' ).show();
    return;
  }
  $( '#NoAppsTR' ).hide();

  var $tableBody = $( '#appTable tbody');

  $.each( appDetailsJSON, function ( index, value ){

    var appCount = index+1;
    var appName = value[0];
    var appId = value[1];
    var appVersion = value[2];
    var appStatus = value[3].charAt(0).toUpperCase() + value[3].slice(1).toLowerCase();
    var appUUID = value[4];

    var labelClass;
    var iconName;

    var pauseTooltipText;
    var pauseDisabled = '';
    var pauseBtnId = 'pauseResume_' + appId;

    var deleteTooltipText;
    var deleteDisabled = '';
    var deleteBtnId = 'delete_' + appId;

    switch ( appStatus )
    {
      case 'Upgrading':
        labelClass = 'label-primary';
        iconName = "fa-pause";
        pauseTooltipText = "Cannot Pause App in Upgrading State";
        pauseDisabled = " disabled";
        deleteTooltipText = "Cannot Delete App in Upgrading State";
        deleteDisabled = " disabled";
        break;
      case 'Creating':
        labelClass = 'label-info';
        iconName = "fa-pause";
        pauseTooltipText = "Cannot Pause Apps in Creating State";
        pauseDisabled = " disabled"
        deleteTooltipText = "Cannot Delete App in Creating State";
        deleteDisabled = " disabled";
        break;
      case 'Running':
        labelClass = 'label-success';
        iconName = "fa-pause";
        pauseTooltipText = "Pause App";
        deleteTooltipText = "Delete App";
        break;
      case 'Stopped':
        labelClass = 'label-warning';
        iconName = "fa-play";
        pauseTooltipText = "Resume App";
        deleteTooltipText = "Delete App";
        break;
      case 'Error':
        labelClass = 'label-danger';
        iconName = "fa-pause";
        pauseTooltipText = "Cannot Pause Apps in Error Stat e";
        pauseDisabled =  " disabled";
        deleteTooltipText = "Delete App";
        break;
    }

    var $tr = $('<tr data-status="' + appStatus + '">').append(
      $('<td>').text(appCount),
      $('<td>').text(appName),
      $('<td>').text(appUUID),
      $('<td>').text(appVersion),
      $('<td>').append($('<span class="label ' + labelClass + '">').text(appStatus)),
        $('<td style="text-align:center;">').append([
        $('<span class="tooltip-wrapper" title="' + pauseTooltipText + '">').append(
          $('<a href="#" id="' + pauseBtnId + '" data-appid="' + appId +'" class="pauseResume" onclick="handleClicks(this)"' + pauseDisabled + '>').append(
            $('<i class="fa ' + iconName + '">')
          )
        )
      , $('<span class="tooltip-wrapper" title="' + deleteTooltipText + '">').append(
          $('<a href="#" id="' + deleteBtnId + '" data-appid="' + appId +'" class= "delete" onclick="handleClicks(this)"' + deleteDisabled + '>').append(
            $('<i class="fa fa-trash">')
          )
        )])
    );

    $tableBody.append( $tr );
  });
}

function handleClicks( e ) {

  var $e= $(e);
  var appID = $e.data("appid");
  var btnClass = $e.attr("class");
  var status = $e.closest('tr').data("status");
  var $child = $e.children()
  var iconClass = $child.attr("class");

  switch ( btnClass )
  {
      case "pauseResume":
            if ( status === "Running" ){
                status = "STOPPED";
            }
            else if ( status == "Stopped" ){
                status = "RUNNING";
            }
            toggleBusy( true, $child, iconClass );

             var startStopAppPromise = startStopApp( appID, status );
              startStopAppPromise.then( function( response )
              {
                if ( response.status === 200 )
                {
                  toggleBusy( false, $child );
                  getAppDetails();
                }
                else
                {
                  console.log("error");
                  toggleBusy( false, $child );
                }
              });
          break;
      case "delete":
            toggleBusy( true, $child, iconClass );

            var deleteAppPromise = deleteApp( appID );
            deleteAppPromise.then( function( response )
              {
                if ( response.status === 200 )
                {
                  toggleBusy( false, $child );
                  getAppDetails();
                }
                else
                {
                  console.log("error");
                  toggleBusy( false, $child );
                }
              });
          break;
  }
  return;
}

function toggleBusy ( busy, element, iconClass ) {
    if ( busy ) {
        $("a").attr("disabled", true);
        element.removeClass().addClass( 'fa fa-spinner fa-pulse' );
    }
    else {
        $("a").attr("disabled", false);
    }
}
