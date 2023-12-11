import os
from dotenv import load_dotenv
import requests
import json
from datetime import datetime, timedelta
import time
import numpy as np


load_dotenv()

API_KEY = os.getenv('CLIENT_HUBSPOT_TOKEN')

import requests


# Modify query string between on deal / contacts

object_type = 'contacts'

url = "https://api.hubapi.com/crm/v3/objects/" + object_type

payload = {}
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + API_KEY
}

#Date Range - pass in date time in the form of (YYYY, MM, DD, HH, mm) 
date_from = datetime(2023, 10, 6, 22, 18) 
date_to = datetime(2023, 11, 6, 0, 0)

# Convert to Hupspot required unix timestamp in miliseconds
date_from = round(time.mktime(date_from.timetuple()) * 1000)
date_to = round(time.mktime(date_to.timetuple()) * 1000)

#Set up filters object
name_var = 'Trevor'


# Initialize empty dictionary for filters
filter_dict = {
  "filterGroups": [
    {
       "filters": [
        {
          "propertyName": "createdate",
          "operator": "GTE",
          "value": date_from
        }
      ]
    }
  ]
}


# Programatically add items to the filter if they exist
     

payload = json.dumps(filter_dict)

# Set up global output vars
all_contacts = list()
count = 0

## Function : get_all_contacts
##  @params url
##  @params contact

##  **TODO**@params get_all - Boolean variable that triggers a pagination handler. Passing get_all will trigger a recursive component of the function designed to run until there is no logner a 'next' link in the pagination property of the response object
##  @returns type dict() -  Contacts in a Python Dictionary obejct

# Conditionally add /search paramater to url if the filters are built
if payload !={} : 
  url = url + '/search'


def get_contacts(url, data, payload):
    
    response = requests.request("POST", url, headers=headers, data=payload)

    result = response.json()

    qty = result['total']

    new_data = result['results']
    
    # Get data from pagination related data from result objects
    p_terms = result['paging']

    # merge two lists
    data = data + new_data
    
    return data

    ##TODO - Configure recursive function to handle pagination. This is currently causing a stack overflow error because there are ~25k pages of contacts
    ##if p_terms['next']['link'] == '' : 
    ##else :  
      ## return get_contacts(p_terms['next']['link'], contacts_updated, count)

    # Recall get contacts within get     
  

print(json.dumps(get_contacts(url, all_contacts, payload), indent=2))