#!/usr/bin/python3
import os
import csv
import pickle
from time import sleep
#import geoplotlib
from geopy.geocoders import Nominatim

# fix Atom path
os.chdir('/home/andres/Programs/python/covid/visualizations/')
#print(os.getcwdb())

#Get coord_list from countries in CSV and save dict
def save_obj(obj, name):
    with open('obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)

def get_info(country):
    retries = 0
    try: # this block need to be reduced
        geolocator = Nominatim(user_agent='myapplication')
        location = geolocator.geocode(country)
        if location != None:
            country_list.append(country)
            return (location.latitude,location.longitude)
            #print(country_list[j] + " " + str(coord_list[j]))
        else: print ("Country " + country + " not found")
        sleep(2)  # be nice to service
    except Exception as e:
        print("Error getting " + country + " data: " + str(e))
        if retries < 3 :
            retries += 1
            sleep(5)
            pass
        else:
            print ("Location for " + country + "could not be found")
            return None


dict = load_obj('country_coords')
#print(dict)

with open('data/full_data.csv') as csvData:
    file = csv.reader(csvData, delimiter=',')#,quoting= csv.QUOTE_ALL, quotechar = '"')
    # Load file from save_obj  count line set to but first you have to save it
    headers = next(file)
    j = 0
    country_list = []
    coord_list =  []
    country = None
    for line in file:
        if line[1] != country: # once per country
            country = line[1]
            #print(country)
            if country in dict:
                    country_list.append(country)
                    coord_list.append((dict[country][0],dict[country][1]))
                    print(country_list[j] + " " + str(coord_list[j]))
                    j += 1
            else:
                print("Looking for country " + country)
                if get_info(country) is not None:
                    coord_list.append((get_info(country)[0],get_info(country)[1]))
                    j += 1

country_dict = {k:v for k,v in zip(country_list,coord_list)}
save_obj(country_dict,'country_coords')
#print(country_dict)
