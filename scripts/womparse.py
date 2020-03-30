#!/usr/bin/python3
# ---------------------------------------------------
# Parses wom tables and send to elastic elasticsearch
# ---------------------------------------------------
import requests
from bs4 import BeautifulSoup
import urllib.request as ur
import json
from datetime import datetime
#from urllib import request, parse
#import pandas as pd

def postDict(data):
    url = "http://elastic:changeme@0.0.0.0:9200/test-data-2/_doc/"
    headers = {"Content-Type":"application/json"}
    post_data = data.encode()# parse.urlencode(data).encode()
    req =  requests.post(url, data=post_data, headers=headers)#, auth=(elastic, changeme))
    if req.reason == "Created":
        return True
    else:
        print("Error sending data to elastic, status code: " + str(req.status_code))
        return False

def get_table():
    url = "https://www.worldometers.info/coronavirus/"
    content = ur.urlopen(url).read()
    soup = BeautifulSoup(content,'html.parser')
    table = soup.find('table',{'id':'main_table_countries_today'})
    return table

table = get_table()
if table is None: #wikitable plainrowheaders sortable
    print("Table not found")
dict_hist = {}    # Collection of tables
parsed_table = {} #  date,type,Data
key_names= []
key = 0
rows = table.find_all('tr')
for row in rows:
    column_marker = 0
    values = []
    date = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
    cols = row.find_all('td')
    if key == 0: # Get value field names
        names = row.find_all('th')
        for i in names:
            key_names.append(i.get_text())
    if cols is not None:
        for column in cols:
            value = column.get_text()
            if value is not None:
                values.append(value.rstrip())
        row_dict = {k:v for k,v in zip(key_names,values)}
        json_data = json.dumps({'date': date, 'dataset_type':'wom_reported', 'data': row_dict})
        if not postDict(json_data):
            print("Something went wrong")
    key += 1
