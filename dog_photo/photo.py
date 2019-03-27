#!/usr/bin/env python3
import cgi
import json
import dog_piccss

form = cgi.FieldStorage()

a = open('dog_piccss.json') as json_data:
    d = json.load(json_data)
    print(d)
 
		print("""
			<html>
			<body>
			<img src="%s">		
			</img>
			</body>
			</html>
			""" % dog_pic)


			
		
