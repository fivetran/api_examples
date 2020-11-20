# Create A Fivetran Connector
# Documentation: https://fivetran.com/docs/rest-api/connectors#createaconnector

import requests
from requests.auth import HTTPBasicAuth

# Enter Your API Credentials
# Documentation: https://fivetran.com/docs/rest-api/getting-started

api_key = "Your Fivetran API Key"
api_secret = "Your Fivetran API Secret"

# Create Base64 Encoded Basic Auth Header
auth = HTTPBasicAuth(api_key, api_secret)

url = "https://api.fivetran.com/v1/connectors"

# Create Request Body
# Ensure That The Connector Config Matches the Specific Config for your Source!
# Documentation: https://fivetran.com/docs/rest-api/connectors/config

body = {
    "service": "criteo",
    "group_id": "projected_sickle",
    "trust_certificates": True,
    "run_setup_tests": True,
    "config": {
        "schema": "criteo",
        "username": "myuser",
        "password": "mypassword",
        "app_token": "myapptoken"
    }
}

response = requests.post(url=url,auth=auth,json=body).json()
print(response)
    