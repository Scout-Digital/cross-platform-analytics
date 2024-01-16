import os
import pygsheets
# import pandas as pd




# @function push_to_gsheets(data, sheet_key, sheet_number):
 # @param data: data to be pushed to google sheets. Function assumes the data is a pandas dataframe
 # @param sheet_key: the key of the google sheet. Can be found in the URL parameter when the google 
    #sheet is open in your browser
 # @param sheet_number: the number of the sheet in the google sheet. Defaults to 0, which is the first sheet in google sheets

def push_to_gsheets(data, sheet_key, **kwargs): 
    G_AUTH = os.getenv('GAUTH_KEY_PATH')
    gc = pygsheets.authorize(service_file=G_AUTH) 

    sn = kwargs.get('sheet_number', 0)

    sh = gc.open_by_key(sheet_key)

    wks = sh[sn]

    #update the first sheet with df, starting at cell B2. 
    wks.append_table(data, start='2', end=None, dimension='ROWS', overwrite=True)



