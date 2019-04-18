import os
from flask import Flask, render_template, session, request, redirect, flash, \
    url_for
import sqlite3 as sql


app = Flask(__name__)
app.secret_key = 'many random bytes' 

@app.route("/")
def hello(): #landing page
    con = sql.connect("stories.db")

    cur = con.cursor()
    #Shows the First and the Last name of the women in a dropdown menu.
    women = cur.execute("""SELECT FirstName, LastName FROM Women""")
    return render_template("index.html", women=women)

@app.route("/search", methods=['GET', 'POST'])
def searchfor(): #uses the selected WOMAN and renders the wiki page
    if request.method == 'POST':
        try:
            woman = request.form['woman']
            #Formating the string which is the output of the value - putting it into a list.
            women_list = woman.split(',')

            first_name = women_list[0]
            last_name = women_list[1]
            

            last_name = last_name.replace(')', '')
            first_name =first_name.replace('(', '')
             
        
            #Define which story should be found in the strories_temp template.
            with sql.connect("stories.db") as con:
                cur = con.cursor()
          
                cur = con.cursor()
                story = cur.execute("""SELECT Story FROM Women WHERE (LastName = {}) AND (FirstName = {}) """.format(last_name, first_name)) 
                
                story_again = None
                for s in story:
                    story_again = str(s[0]) #Removes the ( and '
                con.commit() 
        except: #handle the error if the user doesn't select a name
            flash('Please select a name from the menu')
            return redirect(url_for('hello'))
    return render_template('search.html', story=story_again, first_name=first_name, last_name=last_name)


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

            #PROBLEM: How to insert data from one form into 2 tables if one of them has a foreign key?

             # variable = cur.execute(""" JOIN stories ON Women.WomenID=stories.StrWomenID""")
                # var_new = variable[-1]
                # cur.execute("""INSERT INTO stories (Story,StrWomenID) 
                #     VALUES (?) AND JOIN stories ON Women.WomenID=stories.StrWomenID""", (Story))
                # con.commit()   
                          
                # Insert new value into the database
                cur.execute(""" INSERT INTO Women (FirstName, LastName,Story) 
                    VALUES (?,?,?)""", (FirstName, LastName, Story))
                con.commit()                
                msg = "Your story has successfully been added. Thank you for your contribution."
        except:
            con.rollback()
            msg = "There has been an error, please fill in the form again"
    return render_template("done.html", msg=msg)
    con.close()

if __name__ == "__main__":

    app.run(debug=True)
#,port = 80, address="0.0.0.0"