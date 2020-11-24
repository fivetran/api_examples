# List All Fivetran Groups (Warehouses)
# Documentation: https://fivetran.com/docs/rest-api/groups#listallgroups
# TODO: Create Elegant Paging Mechanism
import time
import json
import requests

from datetime import datetime
from requests.auth import HTTPBasicAuth

# Enter Your API Credentials
# Documentation: https://fivetran.com/docs/rest-api/getting-started

api_key = "Your Fivetran API Key"
api_secret = "Your Fivetran API Secret"

# Create Base64 Encoded Basic Auth Header
auth = HTTPBasicAuth(api_key, api_secret)

# Enter Your Fivetran Group ID From group-management/listAllGroups.py
group_id = "pacification_confetti"

# Create Query Parameters For Pagination
# Documentation: https://fivetran.com/docs/rest-api/pagination
limit = 1000
params = {"limit": limit}

url = "https://api.fivetran.com/v1/groups/{}/connectors".format(group_id)

response = requests.get(url=url, auth=auth, params=params).json()

conn_list = response["data"]['items']

for item in response["data"]['items']:
    print(item['id'])
    url = "https://api.fivetran.com/v1/connectors/{}/force".format(item['id'])

    # Get Watermark For Checking If Updated
    watermark = datetime.utcnow().isoformat()

    response = requests.post(url=url,auth=auth).json()
    print(response)

    check_url = "https://api.fivetran.com/v1/connectors/{}".format(item['id'])

    response = requests.get(url=check_url,auth=auth).json()
    sync_timestamp = datetime.strptime(response["data"]["succeeded_at"],'%Y-%m-%dT%H:%M:%S.%fZ').isoformat()

    while watermark > sync_timestamp:
        response = requests.get(url=check_url,auth=auth).json()
        sync_timestamp = datetime.strptime(response["data"]["succeeded_at"],'%Y-%m-%dT%H:%M:%S.%fZ').isoformat()
        if sync_timestamp < watermark:
            print('timestamp of last sucessful sync (',sync_timestamp,') <= watermark (',watermark,'): retrying in 60s')
            time.sleep(60)

    print('Sync Completed')
