import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()

API_KEY = os.getenv('CLIENT_HUBSPOT_TOKEN')

import requests

url = "https://api.hubapi.com/crm/v3/objects/contacts"

payload = {}
headers = {
  'Authorization': 'Bearer ' + API_KEY
}

# Set up global output vars
all_contacts = list()
count = 0

## Function : get_all_contacts
##  @params url
##  @params contact

##  **TODO**@params get_all - Boolean variable that triggers a pagination handler. Passing get_all will trigger a recursive component of the function designed to run until there is no logner a 'next' link in the pagination property of the response object
##  @returns type dict() - All contacts in a Python Dictionary obejct

# Take in mandatory date range functions and return error if not defined
# Specify date time period term (day, week, month, year)
# Date from and date to based on period term
# Posixt timestamp questions - now variable
# Checkout R package for usage of time variable (.utils / exec)

def get_contacts(url, contacts_start):
    
    response = requests.request("GET", url, headers=headers, data=payload)
    
    result = response.json()
    contacts = result['results']
    
    # Get data from pagination related data from result objects
    p_terms = result['paging']

    # merge two lists
    contacts_updated = contacts_start + contacts
    
    return contacts_updated

    ##TODO - Configure recursive function to handle pagination. This is currently causing a stack overflow error because there are ~25k pages of contacts
    ##if p_terms['next']['link'] == '' : 
    ##else :  
      ## return get_contacts(p_terms['next']['link'], contacts_updated, count)

    # Recall get contacts within get     
  

print(get_contacts(url, all_contacts))


 








