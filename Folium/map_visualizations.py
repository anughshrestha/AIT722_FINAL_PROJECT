import folium
import os
import json
import mysql.connector
from mysql.connector import Error

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

#cursor.execute("select * from restaurant_data where category = \"mexican\"")
#sql = "select * from restaurant_data where state in ('PA', 'IL', 'AZ', 'OH', 'NV', 'NC', 'WI') "
sql = "select * from restaurant_data_staged where category = \"chinese\""
cursor.execute(sql)

restaurant_result = cursor.fetchall()

#create map object
	
m = folium.Map(location=[37.0902,-95.7129], zoom_start=4.5)

category_color_code = [
["mexican", "green"],
["italian", "blue"],
["chinese", "red"],
["japanese", "purple"],
["mediterranean", "orange"],
["indian","darkred"],
["thai", "lightred"],
["middle eastern", "beige"],
["vietnamese","darkblue"],
["greek", "darkgreen"]]
'''
["french","cadetblue"],
["korean","darkpurple"],
["caribbean","white"],
["latin american","pink"],
["pakistani","lightblue"]
]
'''
for row in restaurant_result:
	print(row)
	category = row[2]
	restaurant_name = row[3]
	street_address = row[4]
	city = row[5]
	state = row[6]
	zipcode = row[7]
	rating = float(row[8])
	latittude = row[9]
	longitude = row[10]
	print(category)
	print(rating)

	if category == "mexican":
		print("mexicna found")

	#Global tooltip
	#tooltip = 'Click For More Info'
	tooltip = f"{category}\n"
	tooltip += f"{restaurant_name}\n"
	tooltip += f"{rating}\n"
	tooltip += f"{street_address}\n"
	tooltip += f"{city}\n"
	tooltip += f"{state}\n"
	tooltip += f"{zipcode}\n"
	
	#icon = os.path.join("icons", "mexican.png")
	
	#logoIcon = folium.features.CustomIcon('mexican_round_flag.png', icon_size=(35,30))
	
	for category_list in category_color_code:
		if category_list[0] == category:
			color = category_list[1]
			break
	
	if rating >= 4.0:
		icon = "thumbs-up"
	elif rating < 4.0 and rating > 2.9:
		icon = "minus-sign"
	else:
		icon = "thumbs-down"

	#Markers
	folium.Marker([latittude,longitude],
		popup=f'<strong>{tooltip}</strong>',
		tooltip=tooltip, 
		icon=folium.Icon(color=f'{color}', icon=f'{icon}')).add_to(m)
		#icon=logoIcon).add_to(m)
		#tooltip=tooltip, icon=folium.Icon(color='green')).add_to(m)

#Generate map
m.save('map.html')
	
cursor.close()