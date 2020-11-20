# Sync Data From A Fivetran Connector
# Documentation: https://fivetran.com/docs/rest-api/connectors#syncconnectordatabeta

import requests
from requests.auth import HTTPBasicAuth

# Enter Your API Credentials
# Documentation: https://fivetran.com/docs/rest-api/getting-started

api_key = "Your Fivetran API Key"
api_secret = "Your Fivetran API Secret"

# Create Base64 Encoded Basic Auth Header
auth = HTTPBasicAuth(api_key, api_secret)

# Enter Your Fivetran Connector ID From group-management/listAllConnectorsInGroup.py
connector_id = "Your Fivetran Connector ID"

url = "https://api.fivetran.com/v1/connectors/{}/force".format(connector_id)

response = requests.post(url=url,auth=auth).json()
print(response)
