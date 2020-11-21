import json
import csv
import os

script_dir = os.getcwd() #stores the directory where this script is stored
os.chdir("../") #goes back on directory
root_dir = os.getcwd() #gets the root dir. the directory path right outside the script dir is called root
os.chdir("Dataset") #Make sure there is a dir named Dataset right outside the directory where the script is located
data_set_path = os.getcwd() #the Dataset directory is called data_set_path
os.chdir(script_dir) #navigates back to the script dir

#make sure the json file is downloaded from https://www.yelp.com/dataset
json_source = data_set_path + '\\yelp_academic_dataset_business.json' #make sure the yelp_academic_dataset_business.json file in the data_set_path dir

with open(json_source, 'r', encoding='utf-8') as f: #converts contents of json file into list
	yelp_business_data = [json.loads(line) for line in f] #stores all the contents of the file to the list named yelp_business_data

#writes the data to csv file named restaurant_categories.csv
with open('restaurant_categories.csv', 'w', newline='') as f: 
	writer = csv.writer(f) #uses the methods from csv module to write to the csv file
	for business_data in yelp_business_data:
		categories = str(business_data['categories']) #gets the category of the business

		#it will write to the csv file only when the category contains the words restaurants or cafe
		if "restaurants" in categories.lower() or "cafe" in categories.lower(): 

			business_id = business_data['business_id'] #gets the business id
			rating = float(business_data['stars']) #gets the rating
			latitude = business_data['latitude'] #gets the latitude
			longitude = business_data['longitude'] #gets the longitude
			writer.writerow([business_id, categories, rating,latitude, longitude]) #the data into the each row of csv file





