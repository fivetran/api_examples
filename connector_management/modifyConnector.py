# Modify A Fivetran Connector
# Documentation: https://fivetran.com/docs/rest-api/connectors#modifyaconnector

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

url = "https://api.fivetran.com/v1/connectors/{}".format(connector_id)

# Create Request Body
# Ensure That The Connector Config Contains the Specific Updated Config for your Source
# Documentation: https://fivetran.com/docs/rest-api/connectors/config

body = {
    "paused": False,
    "is_historical_sync": False,
    "sync_frequency": 60,
    "trust_certificates": True,
    "run_setup_tests": True,
    "config": {
        "username": "newuser",
        "password": "newpassword"
    },
    "schedule_type": "manual"
}

response = requests.patch(url=url,auth=auth,json=body).json()
print(response)
