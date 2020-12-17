import csv
import mysql.connector
from mysql.connector import Error
from nltk.tokenize import word_tokenize
import os

script_dir = os.getcwd() #stores the directory where this script is stored
os.chdir("../") #goes back on directory
root_dir = os.getcwd() #gets the root dir. the directory path right outside the script dir is called root
os.chdir("Dataset") #Make sure there is a dir named Dataset right outside the directory where the script is located
data_set_path = os.getcwd() #the Dataset directory is called data_set_path
os.chdir(script_dir) #navigates back to the script dir

median_csv_file = data_set_path + "\\medianIncomeCity.csv"

try:
	connection = mysql.connector.connect(host = 'localhost',
											database = 'zeus',
											user = 'root',
											password = 'Parrot1234',
											auth_plugin='mysql_native_password')

	if connection.is_connected():
		print("Yay! connected")
except Error as e:
	print("Error when connecting to MySQL", e)
	exit()

cursor = connection.cursor()

#reads the CSV file and injects it to the database
with open(median_csv_file, encoding="utf-8") as f:

	csv_reader = csv.reader(f, delimiter=",")
	count = 0
	for row in csv_reader:
		if count > 0:
			if str(row[0]) == "Champaigne":
				metropolitan_area_name = "Urbana"
				city = "Urbana"
			else:
				metropolitan_area_name = str(row[0])
				city = row[0]
			average_income = row[4]
			#city = row[0]
			state = row[1]
			latitude = row[2]
			longitude = row[3]
			print(f"{metropolitan_area_name} {average_income} {city} {state} {latitude} {longitude}")
			sql = "INSERT INTO metropolitan_area_data (metropolitan_area_name, average_income, city, state, latitude, longitude) "
			sql += "values (%s,%s,%s,%s,%s,%s)"

			val = (metropolitan_area_name, average_income, city, state ,latitude,longitude)
			cursor.execute(sql, val)
			connection.commit()
			print(cursor.rowcount, "record inserted.")		
		if count == 8:
			break
		count+=1

cursor.close()