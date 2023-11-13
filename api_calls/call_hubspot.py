import os
import hubspot
from dotenv import load_dotenv
import requests as req

from pprint import pprint
from hubspot.crm.imports import ApiException
from hubspot import hubspot.files

#Import necessary functions from HubSpot python package

from hubspot import HubSpot
# from hubspot import 

from hubspot.auth.oauth import ApiException


rest_base = 'https://api.hubapi.com'

contacts_request_url = '/crm/v3/objects/contacts'


# Get environment variables via dotenv package

load_dotenv()

# API_USERNAME = os.getenv('CLIENT_HUBSPOT_EMAIL')
API_KEY = os.getenv('CLIENT_HUBSPOT_TOKEN')

print(API_KEY)

client = hubspot.Client.create(access_token=API_KEY)

print(client)

try:
    api_response = client.crm.imports.core_api.get_page()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling core_api->get_page: %s\n" % e)





