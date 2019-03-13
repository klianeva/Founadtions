#!/usr/bin/env python3
import cgi
import csv

form = cgi.FieldStorage()
color_input = form.getvalue('color').title()


with open('scripts/colornames.csv', mode="r") as csv_file:
	csv_reader = csv.DictReader(csv_file)
	exist = False
	hexx = None
	for row in csv_reader:
		if color_input == row["name"] or color_input == row["hex"]:
			hexx = row["hex"]
			exist = True

	if exist == True:
		print("""
			<html>
			<body>
			<p>
				%s is a real color and its's hex is: %s
			</p>
			</body>
			</html>
			""" % (color_input, hexx))
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


			
		
