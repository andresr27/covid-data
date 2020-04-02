#!/usr/bin/python3
import os
import csv
import json
#import pickle
#from time import sleep
import geoplotlib
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from geoplotlib.utils import BoundingBox
from geoplotlib.colors import ColorMap
## Need this line so Atom can run it :grrrff
os.chdir('/home/andres/Programs/python/covid/')
from urllib.request import urlopen
# with urlopen('https://github.com/datasets/geo-countries/blob/master/data/countries.geojson') as response:
#     countries = json.load(response)
with open('data/world-countries.json') as file:
    countries = json.load(file)

df = pd.read_csv('data/full_data_enrd.csv',dtype={'name': str})
df.head()
fig = px.choropleth(df, geojson=countries, locations='name', color='total_cases',
           featureidkey="properties.name",
           color_continuous_scale="Reds",
           range_color=(0, 10000),
           scope="world",
           labels={'new_cases':'new cases'}
           )

fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
