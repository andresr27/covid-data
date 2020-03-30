#!/usr/bin/python3
import os
import csv
import pickle
from time import sleep
import geoplotlib
from geopy.geocoders import Nominatim

#Get coord_list from countries in CSV and save dict
def save_obj(obj, name):
    with open('obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name ):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)
# fix Atom path
os.chdir('/home/andres/Programs/python/covid/visualizations/')
#print(os.getcwdb())
with open('full_data.csv') as csvData:
    file = csv.reader(csvData, delimiter=',')#,quoting= csv.QUOTE_ALL, quotechar = '"')
    # Load file from save_obj  count line set to but first you have to save it
    headers = next(file)
    j = 0
    country_list = []
    coord_list =  []
    country = None
    for line in file:
        if line[1] != country:
            country = line[1]
            #print(country)
            try:
                geolocator = Nominatim(user_agent='myapplication')
                location = geolocator.geocode(country)
                if location != None:
                    country_list.append(country)
                    coord_list.append((location.latitude,location.longitude))
                    print(country_list[j] + " " + str(coord_list[j]))
                    j += 1
                else: print ("Country " + country + " not found")
                sleep(1)
            except Exception as e:
                print("Error getting " + country + "'s data: " + str(e))
                sleep(10)
                j -= 1
                ## Count a a few cycles if persists save data and break
                pass
country_dict = {k:v for k,v in zip(country_list,coord_list)}
save_obj(country_dict,'country_coords')
print(country_dict)
