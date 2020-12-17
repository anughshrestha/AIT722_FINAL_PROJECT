There are three parts to the project: Data Preprocessing, Folium Visualization, and Flask
Please follow pre-requiste steps before executing the code for individual sections

******Pre-requistes******

1) Make sure you have Python3 installed in your system
2) Make sure MySQL is installed in your system
3) Create a database named zeus
	i. create database zeus
4) In the MySQL_dump_files directory, find main_schemas_ddl.sql and staged_data.sql
	i. execute the main_schemas_ddl.sql file and staged_data.sql in zeus database
5) Download yelp_academic_dataset_business.json file from Mason Drive and place it in Dataset directory
6) Install the following Python modules using the pip command listed below:
	i. pip install mysql-connector-python
	ii. pip install nltk
	iii. pip install folium
	iv. pip install virtualenv

************************

###Data Preprocessing###
1) yelp_business_json_converter.py (Hence this can take a long time)
	i. creates restaurant_categories.csv
2) most_common_categories.py
	i. creates most_common_categories.csv
3) get_top_categories.py
	i. reads top_categories.txt 
	ii. creates top_restaurant_categories_final.csv
4) restaurant_data_sql_injector.py (Hence this can take a long time)
	i. inserts data into restaurant_data table
	ii. in the script, insert the username and password to connect to MySQL database starting at line 8
5) median_income_sql_injector.py
	i. inserts data into metropolitan_area_data table 
ii. in the script, insert the username and password to connect to MySQL database starting at line 17


###Folium Visualization####
1) A respective Python script is developed to create visualization for the respective restaurant categories
	i. The Python script is named after the restaurant categories that is creating visualization for
2) Each python script generates a html file as the result
	i. These html files were used to create the web-based API in flask

###Flask#####
1) Navigate to the directory named Flask via command prompt or shell terminal
2) Execute: python -m venv venv
3) A directory named venv will be created inside Flask directory
4) Activating the virtual environment
	i. If you are using windows
		a. navigate to venv/Scripts
		b. execute: activate
	ii. If you are using Linux
		a. navigate to venv/bin
		b. execute: . activate
5) Navigate back to Flask directory
6) execute: python app.py runserver
7) You should see an output similar to the one listed below:
* Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 198-623-822
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
8) Type the URL listed below in your web browser
	i. http://127.0.0.1:5000
9) confirm you see the landing page