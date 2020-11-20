# Modify A Fivetran Connector Database Schema Config
# Documentation: https://fivetran.com/docs/rest-api/connectors#modifyaconnectordatabaseschemaconfig

import requests
from requests.auth import HTTPBasicAuth

# Enter Your API Credentials
# Documentation: https://fivetran.com/docs/rest-api/getting-started

api_key = "Your Fivetran API Key"
api_secret = "Your Fivetran API Secret"

# Create Base64 Encoded Basic Auth Header
auth = HTTPBasicAuth(api_key, api_secret)

# Enter Fivetran Connector ID from group-management/listAllConnectorsInGroup.py
connector_id = "Your Fivetran Connector ID"

# Enter Database Schema Name from Source

url = "https://api.fivetran.com/v1/connectors/{}/schemas/reload".format(connector_id)

# Create Request Body
# Reload Using The Proper Exclude Mode
# Documentation: https://fivetran.com/docs/rest-api/connectors#reloadaconnectorschemaconfig

body = {
    "exclude_mode":"EXCLUDE"
}

response = requests.post(url=url,auth=auth,json=body).json()
print(response)