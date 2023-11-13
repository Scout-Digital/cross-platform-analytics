from hubspot import HubSpot
import os
import requests

rest_base = "https://api.hubapi.com/crm/v3/objects/"



api_url = rest_base +  "?limit=100&archived=false"

api_url = "https://jsonplaceholder.typicode.com/todos/1"

response = requests.get(api_url)

print(response.json())


