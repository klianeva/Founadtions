import sqlite3 as sql

import click
from flask import current_app, g
from flask.cli import with_appcontext

con = sql.connect('stories.db')
print "Opened database successfully";

con.close()