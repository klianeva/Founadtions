WORTH-MENTIONING.COM

My project is about showcasing women who the majoirty of the Western societies have ignored in their history books.

Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

Prerequisites

What things you need to install the software and how to install them

- You will need to install python3 & flask 
- You may need to install pip and virtualenv as well


Starting the server:

git clone git@github.com:klianeva/Foundations.git
cd myproject

cd venv 
source bin/activate
cd ..

cd rflask
FLASK_APP=app.py
flask run 

** in case you want to run the server while still in development add *
export FLASK_ENV= development
flask run



Built With
- Flask - The web framework used
- SQLite - Database


Authors
Viktoria Klianeva


