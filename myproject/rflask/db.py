import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext

conn = sqlite3.connect('stories.db')
print "Opened database successfully";

conn.close()