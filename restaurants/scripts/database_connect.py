#!/usr/local/bin/python3

## simple demo script for showing how to connect to an sqlite DB 
# from Python, and run a simple SQL query 

# import the python library for SQLite 
import sqlite3

# connect to the database file, and create a connection object
db_connection = sqlite3.connect('scripts/restaurants.db')

# create a database cursor object, which allows us to perform SQL on the database. 
db_cursor = db_connection.cursor()

# run a first query 
db_cursor.execute("""SELECT restaurants.NAME, neighborhoods.NAME 
                        FROM restaurants INNER JOIN neighborhoods 
                        ON restaurants.NEIGHBORHOOD_ID = neighborhoods.ID
                        WHERE neighborhoods.NAME='Kreuzberg'""")


# store the result in a local variable. 
# this will be a list of tuples, where each tuple represents a row in the table
list_restaurants = db_cursor.fetchall()

def smth(list_restaurants):
	for l in list_restaurants:
		print("""
			<html>
			<body>
			<p><strong>
				- {} : 
			</strong></p>
			</body>
			</html>
			""".format(l))
smth(list_restaurants)
db_connection.close()
