# Sync Data From A Fivetran Connector
# Documentation: https://fivetran.com/docs/rest-api/connectors#syncconnectordatabeta

import requests
import time
import json

from datetime import datetime
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

# Get Watermark For Checking If Updated
watermark = datetime.utcnow().isoformat()

response = requests.post(url=url,auth=auth).json()
print(response)

check_url = "https://api.fivetran.com/v1/connectors/{}".format(connector_id)

response = requests.get(url=check_url,auth=auth).json()
sync_timestamp = datetime.strptime(response["data"]["succeeded_at"],'%Y-%m-%dT%H:%M:%S.%fZ').isoformat()

while watermark > sync_timestamp:
    response = requests.get(url=check_url,auth=auth).json()
    sync_timestamp = datetime.strptime(response["data"]["succeeded_at"],'%Y-%m-%dT%H:%M:%S.%fZ').isoformat()
    if sync_timestamp < watermark:
        print('timestamp of last sucessful sync (',sync_timestamp,') <= watermark (',watermark,'): retrying in 60s')
        time.sleep(60)

print('Sync Completed')