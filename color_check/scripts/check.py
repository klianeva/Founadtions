#!/usr/bin/env python3
import cgi
import csv

form = cgi.FieldStorage()
color_input = form.getvalue('color').title()


with open('scripts/colornames.csv') as csv_file:
	csv_reader = csv.DictReader(csv_file)

	exist = False
	for row in csv_reader:
		 if color_input == row["name"] or color_input == row["hex"]: 
		 	exist == True
	
	if exist == True:
		print("""
			<html>
			<body>
			<p>
				%s is a real color
			</p>
			</body>
			</html>
			""" % color_input)
	else: 
		print("""
			<html>
			<body>
			<p>
				%s is not a color
			</p>
			</body>
			</html>
			""" % color_input)


			
		
