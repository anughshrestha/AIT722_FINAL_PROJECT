import csv
import mysql.connector
from mysql.connector import Error
from nltk.tokenize import word_tokenize

#connecting to MySQL database. insert username and password to connect your MySQL database
try:
	connection = mysql.connector.connect(host = 'localhost',
											database = 'zeus',
											user = '<removed>',
											password = '<removed>',
											auth_plugin='mysql_native_password')

	if connection.is_connected():
		print("Yay! connected")
except Error as e:
	print("Error when connecting to MySQL", e)
	exit()

cursor = connection.cursor()

count = 0
#reads data from top_restaurant_categories_final.csv and injects it to the MySQL database
with open("top_restaurant_categories_final.csv",encoding="utf-8") as f:

	csv_reader = csv.reader(f, delimiter=",")
	for row in csv_reader:
		business_id = row[0]
		category = row[1]
		name = row[2]
		street_address = row[3]
		city = row[4]
		state = row[5]
		zipcode = row[6]
		rating = row[7]
		latitude = row[8]
		longitude = row[9]
		sql = "INSERT INTO restaurant_data (business_id, category, restaurant_name, address, city, state, zipcode,rating, latitude, longitude) "
		sql += "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

		val = (business_id, category, name, street_address, city, state, zipcode, rating,latitude,longitude)

		cursor.execute(sql, val)
		connection.commit()
		print(cursor.rowcount, "record inserted.")
		count+=1
print(f"Total Records Inserted: {count}")
cursor.close()
