#!/usr/bin/python3
import os
import csv
import pickle
#from time import sleep
import geoplotlib

def load_obj(name):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)
## Need this line so Atom can run it
os.chdir('/home/andres/Programs/python/covid/visualizations/')
print(os.getcwdb())

def get_coords(country):
    country_dict = load_obj('country_coords')
    if country in country_dict:
        return country_dict[country]
    else: return False

with open('data/full_data.csv') as csvData:
    file = csv.reader(csvData, delimiter=',')#,quoting= csv.QUOTE_ALL, quotechar = '"')
    headers = next(file)
    headers.append('lat')
    headers.append('lon')
    writer = csv.DictWriter(csvData, fieldnames=headers)
    writer.writeheader()
    #print(headers)
    i = 1
    country_list = []
    coord_list =  []
    country = None
    for line in file:
        #if line[1] != country:
        country = line[1]
        country_list.append(country)
        if get_coords(country):
            line.append(get_coords(country)[0]) # append lat from tuple
            line.append(get_coords(country)[1]) # append lon from tuple
        writer.writerow(line)
        print(line)
        i += 1

#geolocator = Nominatim(user_agent='myapplication')
#location = geolocator.geocode("Uruguay")
#print(location.latitude)

# data = geoplotlib.utils.read_csv('COVID-GDDW.csv')
# geoplotlib.dot(data)
# geoplotlib.show()
