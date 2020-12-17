import csv

'''
Method: top_categories
Parameters: None
Returns: categories_list (list)
Purpose: reads the top_categories.txt and stores it into a list. top_categories.txt file contains the list of 
most frequent occuring categories in the dataset.
'''
def top_categories():

	categories = open("top_categories.txt", "r") #opens top_categories.txt file and stores it to categories variable
	categories_list = [] #list to store the contents of the file
	for cat in categories: #loops through the categories list
		cat_item = cat.rstrip().lstrip() #clears space from each items in the list
		categories_list.append(cat_item) #appends the item to the categories_list list
	return categories_list

'''
Method: export_top_categories_to_csv
Parameters: top_categories (list)
Returns: None
Purpose: exports the data from top_categories list to a csv file
'''
def export_top_categories_to_csv(top_categories):

	with open("restaurant_categories.csv", encoding="utf-8") as f: #reads the data from restaurant_categories.csv file
		file_row = csv.reader(f, delimiter=",") #uses the reader method from csv module to read the data from csv file and stores it to file_row variable

		with open('top_restaurant_categories_final.csv', 'w', newline='',encoding="utf-8") as f: #writes the data from top_categories to top_restaurant_categories_final.csv
			writer = csv.writer(f) #uses the writer method from csv module to write to top_restaurant_categories_final.csv

			for row in file_row: #loops through file_row list
				'''
				row[1] contains the list of restaurant categories. Uses the split function to split the categories into a list.
				The list of categories are passed to the clean_words method. Details listed below.
				clean_words method returns a list and stored to categories variable
				'''
				categories = clean_words(row[1].lower().split(",")) 

				'''
				loops through categories list. 
				if the category exists in the top_categories list then it writes to the top_restaurant_categories_final.csv file
				if a restaurant contains several categories from the top_categories list then it will create seperate entries for each entry
				For example: if a restaurant contains Chinese and Japanese as category, it will create two seperate entries. It will create an
				entry where the category is Chinese and another for where the category is Japanese
				'''
				for category in categories:
					if category in top_categories:
						writer.writerow([row[0],category,row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]])

'''
Method: clean_words
Parameters: list_words (list)
Purpose: this method ensures are certains unuseful categories are excluded from the bag of words.
The list of words are listed in the method. This method also removes spaces from the items in list_words list 
that is passed on as parameter.
Returns: list_words (list)
'''
def clean_words(list_words):
	exclusion_list = ['restaurants', 
					  'food', 'cafes', 
					  'event planning & services',
					  'venues & event spaces',
					  'hotels & travel',
					  'beauty & spas', 
					  'american (traditional)',
					  'american (new)'
					]
	count = 0
	for word in list_words:
		
		list_words[count] = str(word.rstrip().lstrip())
		word = str(word.rstrip().lstrip())
		count+=1

	for exclusion in exclusion_list:

		try:
			list_words.remove(exclusion)
		except ValueError:
			print(f"{exclusion} not found")
	

	return list_words
'''
Method: main
'''
def main():

	top_categories_restaurants = top_categories() #calls top_categories
	export_top_categories_to_csv(top_categories_restaurants) #calls export_top_categories_to_csv

main()