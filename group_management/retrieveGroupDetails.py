# Retrieve Group Details (Warehouses)
# Documentation: https://fivetran.com/docs/rest-api/groups#retrievegroupdetails

import requests
from requests.auth import HTTPBasicAuth

# Enter Your API Credentials
# Documentation: https://fivetran.com/docs/rest-api/getting-started

api_key = "Your Fivetran API Key"
api_secret = "Your Fivetran API Secret"

# Create Base64 Encoded Basic Auth Header
auth = HTTPBasicAuth(api_key, api_secret)

# Enter Your Fivetran Group ID From group-management/listAllGroups.py
group_id = "solicit_shock"

url = "https://api.fivetran.com/v1/groups/{}".format(group_id)

response = requests.get(url=url, auth=auth).json()

print(response)