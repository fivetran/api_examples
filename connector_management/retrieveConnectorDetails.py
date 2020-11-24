# Retrieve A Fivetran Connector Details (including Config)
# Documentation: https://fivetran.com/docs/rest-api/connectors#retrieveconnectordetails

import requests
from requests.auth import HTTPBasicAuth

# Enter Your API Credentials
# Documentation: https://fivetran.com/docs/rest-api/getting-started

api_key = "Your Fivetran API Key"
api_secret = "Your Fivetran API Secret"

# Create Base64 Encoded Basic Auth Header
auth = HTTPBasicAuth(api_key, api_secret)

# Enter Fivetran Connector ID from group-management/listAllConnectorsInGroup.py
connector_id = "paralyses_budding"

url = "https://api.fivetran.com/v1/connectors/{}".format(connector_id)

response = requests.get(url=url,auth=auth).json()
print(response)
