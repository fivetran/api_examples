# Overview
These examples are designed as standalone scripts that act as examples for interacting with our REST API.

> Please Note: These are representative samples, and should **not** be used in production implementaions "as is".

# Common Use Cases
 > I want to sync a connector using an external orchestration tool.


1. [List All Groups](group-management/listAllGroups.py)
2. [List All Connectors In Group](group-management/listAllConnectorsInGroup.py)
3. [Sync Connector Data](connector-management/syncConnectorData.py)

![](../../resources/images/api-sync-connector-flow.png)

> I want to manage schema for a database using only the API (after setting up connection in UI)
1. [List All Groups](group-management/listAllGroups.py)
2. [List All Connectors In Group](group-management/listAllConnectorsInGroup.py)
3. [Reload Connector Schema Config](connector-management/reloadConnectorSchemaConfig.py) setting `exclusion_mode = EXCLUDE`
4. [Modify Connector Database Schema Config](connector-management/modifyConnectorDatabaseSchemaConfig.py) with just the schema/table you would like

# Directory Contents

## [Group Management](https://github.com/fivetran/api_examples/blob/master/resources/images/api-sync-connector-flow.png)

These scripts are a subset of the available endpoints with the group management endpoints. They are some of the most frequently used endpoints, and will be used in getting `group_id`s and `connector_id`s for usage in the connector management scripts. 

[Link to Docs](https://fivetran.com/docs/rest-api/groups)

### Scripts
- [List All Groups](group-management/listAllGroups.py)
- [Retrieve Group Details](group-management/retrieveGroupDetails.py)
- [List All Connectors In Group](group-management/listAllConnectorsInGroup.py)

## [Connector Managemement](connector-management)

These scripts are designed to interact with individual endpoints that provide control over some of the basic operations that Fivetran allows. As with the Group Managment section above, the scripts provided do not provide full coverage of the available endpoints. 

[Link to Docs](https://fivetran.com/docs/rest-api/groups)

### Scripts
- [Create Connector](connector-management/createConnector.py)
- [Delete Connector](connector-management/deleteConnector.py)
- [Modify Connector](connector-management/modifyConnector.py)
- [Retrieve Connector Details](connector-management/retrieveConnectorDetails.py)
- [Sync Connector Data](connector-management/syncConnectorData.py)
- [Sync Connector Data Return](connector-management/syncConnectorDataReturn.py)
- [Reload Connector Schema Config](connector-management/reloadConnectorSchemaConfig.py)
- [Modify Connector Database Schema Config](connector-management/modifyConnectorDatabaseSchemaConfig.py)
