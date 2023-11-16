import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.getenv('CLIENT_HUBSPOT_TOKEN')

import requests

url = "https://api.hubapi.com/crm/v3/objects/contacts"

payload = {}
headers = {
  'Authorization': 'Bearer ' + API_KEY

}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)









