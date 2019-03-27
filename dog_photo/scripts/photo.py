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
			<p style="font:Verdana; font-size:20px; margin-top: 30px; margin-left:30px;"><strong>
				%s is a real color and its's hex is: %s
			</strong></p>
			<div style="background-color:%s; width:300px; height:50px; float:left; margin-left:30px;">
			</div>
			</body>
			</html>
			""" % (color_input, hexx, hexx))
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


			
		
