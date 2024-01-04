import os
from dotenv import load_dotenv
import requests
import json
from datetime import datetime, timedelta
import time
import numpy as np
import pytz as tz

timezone = 'America/Chicago'

load_dotenv()

API_KEY = os.getenv('CLIENT_HUBSPOT_TOKEN')

# Modify query string between on deal / contacts

object_type = 'contacts'

url = "https://api.hubapi.com/crm/v3/objects/" + object_type

payload = {}
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + API_KEY
}



#Date Range - pass in date time in the form of (YYYY, MM, DD, HH, mm). 
date_from = datetime(2023, 10, 6, 22, 18)
date_to = datetime(2023, 11, 6, 0, 0) or datetime.now()

# set timezone 
date_from = tz.timezone(timezone).localize(date_from)
date_to = tz.timezone(timezone).localize(date_to)



# Convert to Hupspot required unix timestamp in miliseconds
date_from = round(time.mktime(date_from.timetuple()) * 1000)
date_to = round(time.mktime(date_to.timetuple()) * 1000)

#Set up filters object
name_var = 'Trevor'


# Initialize dictionary for filters with required parameters. Date to and date from must be set.
# If no value exists for date_to, default to present datetime
filter_dict = {
  "filterGroups": [
    {
       "filters": [
        {
          "propertyName": "createdate",
          "operator": "GTE",
          "value": date_from
        },
        {
          "propertyName": "createdate",
          "operator": "LTE",
          "value": date_to
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



# Conditionally add /search paramater to url if the filters are built
if payload !={} : 
  url = url + '/search'

## Function : get_contacts
##  @params url: type string
##  @params data: type pass in empty list()
##  @params payload: filter dictionary. Date to and date from are required

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

    ##TODO - Configure recursive function to handle pagination. This is currently causing a stack overflow error because there are ~25k pages of contacts in the sample data
    ##if p_terms['next']['link'] == '' : 
    ##else :  
      ## return get_contacts(p_terms['next']['link'], contacts_updated, count)

    # Recall get contacts within get     
  

export_data = json.dumps(get_contacts(url, all_contacts, payload), indent=2)

print(export_data)