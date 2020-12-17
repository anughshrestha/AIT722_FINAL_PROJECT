import csv
from nltk.tokenize import word_tokenize
import nltk

'''
Method: get_categories_bow
Parameters: None
Purpose: creates bag of word of all the categories of restaurants that are in the dataset
Returns: bow_categories
'''
def get_categories_bow():
	bow_categories = [] #list that stores the bag of words of all the categories of restaurants
	with open("restaurant_categories.csv", encoding="utf8") as f: #opens restaurant_categories.csv
		file_row = csv.reader(f, delimiter=",") #uses the reader method from csv file to read each row of csv file
		for row in file_row:
			'''
			row[1] contains the list of restaurant categories. Uses the split function to split the categories into a list.
			The list of categories are passed to the clean_words method. Details listed below.
			clean_words method returns a list and stored to categories variable
			'''
			categories = clean_words(row[1].lower().split(",")) 

			#loops through categories list and appends it to the bow_categories list
			for category in categories:
				bow_categories.append(category)

	return bow_categories

'''
Method: clean_words
Parameters: list_words (list)
Purpose: this method ensures are certains unuseful categories are excluded from the bag of words.
The list of words are listed in the method. This method also removes spaces from the items in list_words list 
that is passed on as parameter.
Returns: list_words (list)
'''
def clean_words(list_words):
	#These are list of unuseful categories that will be excluded from the BOW
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
	for word in list_words: #removes the spaces from the list_words
		list_words[count] = str(word.rstrip().lstrip())
		word = str(word.rstrip().lstrip())
		count+=1

	#if the list_words contains the items that are listed in the exclusion_list then those items are exluded. 
	for exclusion in exclusion_list: 
		try:
			list_words.remove(exclusion)
		except ValueError:
			print(f"{exclusion} not found")
	

	return list_words

'''
Method: get_most_common
Parameters: bow_categories (list)
Purpose: calculates frequency distribution of the categories in BOW by using nltk module
Returns: frequent_dist (list)
'''
def get_most_common(bow_categories):

	frequent_dist = nltk.FreqDist(bow_categories) #uses the FreqDist method from nltk to get the frequency dist
	return frequent_dist

'''
Method: export_most_common
Parameters: most_common_categories_freq_dist (list)
Purpose: exports the data from most_common_categories_freq_dist into a csv file
Returns: None
'''
def export_most_common(most_common_categories_freq_dist):

	with open('most_common_categories.csv', 'w', newline='', encoding='utf-8') as f:
		writer = csv.writer(f)
		for most_common in most_common_categories_freq_dist.most_common():
			writer.writerow([most_common[0],most_common[1]])

'''
These are the list of most frequently occuring international restaurant categories that appear in the dataset.
They were pulled manually from the most_common_categories.csv file and placed in top_categories.txt

Top Restaurants:
mexican
italian
chinese
japanese
mediterranean
indian
thai
middle eastern
vietnamese
greek
french
korean
'''

'''
Method: main()
'''
def main():
	bow_categories = get_categories_bow() #calls get_categories_bow method
	most_common_categories_freq_dist = get_most_common(bow_categories) #calls get_most_common
	export_most_common(most_common_categories_freq_dist) #calls export_most_common

main()