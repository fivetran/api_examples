# List All Fivetran Groups (Warehouses)
# Documentation: https://fivetran.com/docs/rest-api/groups#listallgroups
# TODO: Create Elegant Paging Mechanism

import requests
from requests.auth import HTTPBasicAuth

# Enter Your API Credentials
# Documentation: https://fivetran.com/docs/rest-api/getting-started

api_key = "Your Fivetran API Key"
api_secret = "Your Fivetran API Secret"

# Create Base64 Encoded Basic Auth Header
auth = HTTPBasicAuth(api_key, api_secret)

# Enter Your Fivetran Group ID From group-management/listAllGroups.py
group_id = "propensity_broadly"

# Create Query Parameters For Pagination
# Documentation: https://fivetran.com/docs/rest-api/pagination
limit = 1000
params = {"limit": limit}

url = "https://api.fivetran.com/v1/groups/{}/connectors".format(group_id)

response = requests.get(url=url, auth=auth, params=params).json()
print(response)

conn_list = response["data"]['items']

while "next_cursor" in response["data"]:
    print("paged")
    params = {"limit": limit, "cursor": response["data"]["next_cursor"]}
    response_paged = requests.get(url=url, auth=auth, params=params).json()
    if any(response_paged["data"]["items"]) == True:
        conn_list.extend(response_paged["data"]['items'])
    response = response_paged

print(conn_list)
