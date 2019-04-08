import os
from flask import Flask, render_template, session 


app = Flask(__name__)

@app.route("/")
def hellow():
	return "Hello"

def factors(num):
	return [x for x in range (1, num+1) if num%x==0]

@app.route("/factors/<int:n>")
def factors_route(n):
	return render_template(
		"factors.html",  # name of template
		number=n,  # value for `number` in template
		factors=factors(n) # value for `factors` in template
	)



if __name__ == "__main__":

    app.run(debug=True,port = 80, address="0.0.0.0")
