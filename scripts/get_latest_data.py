#!/usr/bin/python3
import os
import csv
import urllib.request as ur

os.chdir('/home/andres/Programs/python/covid/visualizations/')
#print(os.getcwdb())
url = "https://covid.ourworldindata.org/data/ecdc/full_data.csv"
content = ur.urlopen(url).read()
