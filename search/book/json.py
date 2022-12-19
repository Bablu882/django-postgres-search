# # import csv
# # import json
 
# # def csv_to_json(csv_file_path, json_file_path):
# #     #create a dictionary
# #     data_dict = {}
 
# #     #Step 2
# #     #open a csv file handler
# #     with open(csv_file_path, encoding = 'utf-8') as csv_file_handler:
# #         csv_reader = csv.DictReader(csv_file_handler)
 
# #         #convert each row into a dictionary
# #         #and add the converted data to the data_variable
 
# #         for rows in csv_reader:
 
# #             #assuming a column named 'No'
# #             #to be the primary key
# #             key = rows['Serial Number']
# #             data_dict[key] = rows
 
# #     #open a json file handler and use json.dumps
# #     #method to dump the data
# #     #Step 3
# #     with open(json_file_path, 'w', encoding = 'utf-8') as json_file_handler:
# #         #Step 4
# #         json_file_handler.write(json.dumps(data_dict, indent = 4))
 
# # #driver code
# # #be careful while providing the path of the csv file
# # #provide the file path relative to your machine
 
# # #Step 1
# # csv_file_path = input('Enter the absolute path of the CSV file: ')
# # json_file_path = input('Enter the absolute path of the JSON file: ')
 
# # csv_to_json(csv_file_path, json_file_path)


# import json
# import csv


# with open ('fixtures/books.csv','r') as f:
#     reader=csv.reader(f)
#     next(reader)
#     data =[]
#     for row in reader:
#         data.append({
#             'model':row[0],
#             'id':row[1],
#             'title':row[2],
#             'authors':row[3]

#         })

# with open('fixtures/books.json','w') as f:
#     json.dump(data,f,indent=4)        


import csv
import json


# Function to convert a CSV to JSON
# Takes the file paths as arguments
def make_json(csvFilePath, jsonFilePath):
	
	# create a dictionary
	data = {}
	
	# Open a csv reader called DictReader
	with open(csvFilePath, encoding='utf-8') as csvf:
		csvReader = csv.DictReader(csvf)
		
		# Convert each row into a dictionary
		# and add it to data
		for rows in csvReader:
			
			# Assuming a column named 'No' to
			# be the primary key
			key = rows['']
			data[key] = rows
   

	# Open a json writer, and use the json.dumps()
	# function to dump data
	with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
		jsonf.write(json.dumps(data, indent=4))
		
# Driver Code

# Decide the two file paths according to your
# computer system
csvFilePath = r'fixtures/books.csv'
jsonFilePath = r'fixtures/bookss.json'

# Call the make_json function
make_json(csvFilePath, jsonFilePath)
