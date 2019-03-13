import csv
exist = False
color_input = "Yellow"
with open('colornames.csv', mode="r") as csv_file:
	csv_reader = csv.DictReader(csv_file)
	for row in csv_reader:
		if color_input == row["name"] or color_input == row["hex"]: 
			print(row["hex"])