/**
Licensed Materials - Property of IBM
5725I71-CC011829
(C) Copyright IBM Corp. 2017, 2018. All Rights Reserved.
US Government Users Restricted Rights - Use, duplication or
disclosure restricted by GSA ADP Schedule Contract with IBM Corp.
 */



function my_offense_toolbar_button_action(offense)
{
    var content_from_view = offense.custom_data_from_python_view;
    var selected_row_ids = QRadar.getSelectedRows().toString();

    if (!selected_row_ids)
    {
        selected_row_ids = "None";
    }

    alert ("Selected row IDs: " + selected_row_ids
    + "\nContent from python view: " + content_from_view);
}
