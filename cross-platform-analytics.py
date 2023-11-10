import requests
import os

rest_base = "https://api.hubapi.com/crm/v3/objects/"

client_api_token = os.environ.get('HUBSPOT_API_KEY')

api_url = rest_base +  "?limit=100&archived=false"

api_url = "https://jsonplaceholder.typicode.com/todos/1"

response = requests.get(api_url)

print(response.json())