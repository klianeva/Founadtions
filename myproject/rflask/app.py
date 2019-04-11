import os
from flask import Flask, render_template, session, request
import sqlite3 as sql

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")


@app.route('/enternew')
def new_story():
   return render_template('stories_temp.html')

@app.route("/addstr", methods = ['POST', 'GET'])
def addstr():
    if request.method == 'POST':
        try:
            FirstName = request.form['FirstName']
            LastName = request.form['LastName']
            Story = request.form['Story']
        
            with sql.connect("stories.db") as con:
                cur = con.cursor()

            # sql_statement_one = """INSERT INTO women(FirstName,LastName) 
            #   VALUES (?,?)""";
            # sql_statement_two = """INSERT INTO stories(Story) 
            #   VALUES (?)""";

            #PROBLEM: How to insert data from one form into 2 tables?

             # variable = cur.execute(""" JOIN stories ON Women.WomenID=stories.StrWomenID""")
                # var_new = variable[-1]
                # cur.execute("""INSERT INTO stories (Story,StrWomenID) 
                #     VALUES (?) AND JOIN stories ON Women.WomenID=stories.StrWomenID""", (Story))
                # con.commit()   
                          
                # 
                
                cur.execute(""" INSERT INTO Women (FirstName, LastName,Story) 
                    VALUES (?,?,?)""", (FirstName, LastName,Story))
                con.commit()                
                msg = "Your story has successfully been added"
        except:
            con.rollback()
            msg = "error damn it"
    return render_template("done.html", msg= msg)
    con.close()

if __name__ == "__main__":
    app.run(debug=True)
#,port = 80, address="0.0.0.0"