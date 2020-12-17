import folium
import os
import json
import mysql.connector
from mysql.connector import Error

#This script creates an empty map for the index page
#create map object
	
m = folium.Map(location=[37.0902,-95.7129], zoom_start=4.5)

#Generate map
m.save('index.html')
