import csv
exist = False
color_input = "Abbey"
with open('./colornames.csv') as csv_file:
	csv_reader = csv.DictReader(csv_file)

	
	for row in csv_reader:
		if color_input is row["name"]: 
		 	exist == True
print(exist) 
	