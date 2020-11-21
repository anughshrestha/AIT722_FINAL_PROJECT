import csv
import mysql.connector
from mysql.connector import Error
from nltk.tokenize import word_tokenize

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

count = 0
with open("top_restaurant_categories_final.csv") as f:

	csv_reader = csv.reader(f, delimiter=",")
	for row in csv_reader:
		business_id = row[0]
		category = row[1]
		rating = row[2]
		latitude = row[3]
		longitude = row[4]
		sql = "INSERT INTO restaurant_data (business_id, category, rating, latitude, longitude) "
		sql += "values (%s,%s,%s,%s,%s)"

		val = (business_id, category,rating,latitude,longitude)

		cursor.execute(sql, val)
		connection.commit()
		print(cursor.rowcount, "record inserted. ")
		count+=1
print(f"Total Records Inserted: {count}")
cursor.close()