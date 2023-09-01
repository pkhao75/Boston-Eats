#Boston Eats
#Recommendation for Boston based restaurant by category/cuisine, price, or location
import csv
from node import Node
from sorting import restaurant_sort

stations = []
def restaurant_from_csv():
	res_dict = {}
	with open('BosEatsCSV.tsv') as restaurants_csv:
	  books_reader = csv.DictReader(restaurants_csv, delimiter = '\t')
	  for row in books_reader:
	  	res_dict[row['Name']] = Node(row['Name'],row['Keyword'],row['Price'],row['Rating'],row['Address'],row['T Line'],row['Location'])
	  	if row['Location'] not in stations:
	  		stations.append(row['Location'])
	  return res_dict

def print_restaurant(restaurants):
	print('=================================================')
	for restaurant in restaurants:
		print(restaurant_list[restaurant])

def first_prompt():
	criteria = {'1': 'by keyword(eg. lunch, alcohol, asian, etc.)', '2':'by price rating', '3':'by closest MBTA station'}
	ans = ['1','2','3']
	print('How would you like to search for a restaurant?')
	print('''Please pick your search criteria:
	1){}
	2){}
	3){}'''.format(criteria['1'],criteria['2'],criteria['3']))
	choice = input('Please enter the number corresponding to your choice: ')
	if choice in criteria :
		ans.remove(choice)
		print('You select search ' + criteria.pop(choice))
		search_results = restaurant_search(restaurant_list, choice)
		prompt = input('Would you like to sort your results?, Enter y/n: ')
		if prompt == 'y':
			result_sort(search_results)
		prompt = input('Would you like to narrow your search down with another criteria?, Enter y/n: ')
		if prompt == 'y':
			choice = second_prompt(criteria,ans)
			search_results = restaurant_search(search_results, choice)

	else:
		print("The answer was not '1', '2', or '3'! Let's try again\n")
		first_prompt()
		
def second_prompt(criteria,ans):
	print('How would you like to narrow down your search results for a restaurant?')
	print('''Please pick your search criteria:
	1){}
	2){}'''.format(criteria[ans[0]],criteria[ans[1]]))
	choice = input('Please enter the number corresponding to your choice: ')
	if choice in ['1','2']:
		second_choice = ans[int(choice)-1]
		print('You select search ' + criteria.pop(second_choice))
	else:
		print("The answer was not '1' or '2'! Let's try again\n")
		second_choice = second_prompt(criteria,ans)
	return second_choice

def restaurant_search(restaurants_dict, search_criteria):
	results = []
	if search_criteria == '1':
		key = input('Please enter search keyword: ')
	elif search_criteria == '2':
		key = input('Please enter price criteria(anycombination of number between 1-3 eg. 12, 31: ')
	else:
		print('Available stations on file:')
		for station in stations:
			print(station)		
		key = input('Please enter the MBTA station you would like to use for searching: ')
	for restaurant in restaurants_dict:
		if search_key(restaurant, key, search_criteria):
			results.append(restaurant)
			#print(restaurant_list[restaurant])
	if len(results) < 1:
		print('Sorry, no restaurant matches your search')
	print_restaurant(results)
	return results

def search_key(restaurant, key, criteria):
	if criteria == '1': return key in restaurant_list[restaurant].key
	elif criteria == '2': return restaurant_list[restaurant].price in key
	else: return key.lower() in restaurant_list[restaurant].tstop.lower()

def result_sort(results):
	list_length = len(results)-1
	print('''Please pick your sorting criteria:
	1)by name
	2)by price
	3)by rating''')
	criteria = input('Please enter the number corresponding to your choice: ')
	if criteria in ['1','2','3']:
		print('''Please pick how you want your sort results to be shown:
	1)ascending
	2)descending''')
		order = input('Please enter the number corresponding to your choice: ')
		if order in ['1','2']:
			if order == '1':
				if criteria == '1': restaurant_sort(results,0, list_length, sort_name_ascending)
				elif criteria == '2': restaurant_sort(results,0, list_length, sort_price_ascending)
				else: restaurant_sort(results,0, list_length, sort_rating_ascending)
				print_restaurant(results)
			elif order == '2':
				if criteria == '1': restaurant_sort(results,0, list_length, sort_name_descending)
				elif criteria == '2': restaurant_sort(results,0, list_length, sort_price_descending)
				else: restaurant_sort(results,0, list_length, sort_rating_descending) 
				print_restaurant(results)
			prompt = input('Would you like to change the result sorting?, Enter y/n: ')
			if prompt == 'y': result_sort(results)
			return
	print('Invalid input, please try again!')
	result_sort(results)

def sort_name_ascending(restaurant_a,restaurant_b):
	return restaurant_list[restaurant_a].name_lower > restaurant_list[restaurant_b].name_lower

def sort_name_descending(restaurant_a,restaurant_b):
	return restaurant_list[restaurant_a].name_lower < restaurant_list[restaurant_b].name_lower

def sort_price_ascending(restaurant_a,restaurant_b):
	return restaurant_list[restaurant_a].price > restaurant_list[restaurant_b].price

def sort_price_descending(restaurant_a,restaurant_b):
	return restaurant_list[restaurant_a].price < restaurant_list[restaurant_b].price

def sort_rating_ascending(restaurant_a,restaurant_b):
	return restaurant_list[restaurant_a].rating > restaurant_list[restaurant_b].rating

def sort_rating_descending(restaurant_a,restaurant_b):
	return restaurant_list[restaurant_a].rating < restaurant_list[restaurant_b].rating




def Boston_Eats():	
	print('Welcome to Boston Eats')
	print('A recommendation system for food around Boston, Massachusetts')
	again = True
	first_prompt()
	while again:
		prompt = input("Would you like to make another restaurant search?, Enter y/n: ")
		if prompt == 'y':
			first_prompt()
		else:
			again = False
			print('=================================================\n')
			print('Thank you for choosing Boston Eats. Enjoy your meal!!!')
			print('\n=================================================')




restaurant_list = restaurant_from_csv()
Boston_Eats()




