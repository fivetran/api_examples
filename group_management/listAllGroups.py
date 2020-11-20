# List All Fivetran Groups (Warehouses)
# Documentation: https://fivetran.com/docs/rest-api/groups#listallgroups

import requests
from requests.auth import HTTPBasicAuth

# Enter Your API Credentials
# Documentation: https://fivetran.com/docs/rest-api/getting-started

api_key = "rsJNOf96zRk9a7xo"
api_secret = "s1ihokmAALdI9UzGEgv4VtosbBphkMik"

# Create Base64 Encoded Basic Auth Header
auth = HTTPBasicAuth(api_key, api_secret)

# Create Query Parameters For Pagination
# Documentation: https://fivetran.com/docs/rest-api/pagination
limit = 1000
params = {"limit": limit}

url = "https://api.fivetran.com/v1/groups"

response = requests.get(url=url, auth=auth, params=params).json()

group_list = response["data"]['items']

while "next_cursor" in response["data"]:
    print("paged")
    params = {"limit": limit, "cursor": response["data"]["next_cursor"]}
    response_paged = requests.get(url=url, auth=auth, params=params).json()
    if any(response_paged["data"]["items"]) == True:
        group_list.extend(response_paged["data"]['items'])
    response = response_paged

print(group_list)