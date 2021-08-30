from app import DB_NAME
import sqlite3
import json

DB_NAME = 'counter.db'
with open('./config.json') as conf:
    app_info = conf.read()
    app_info = json.loads(app_info)
    DB_NAME = app_info['dbname']


with open('./schema.sql', 'r')  as f:
    scripts = f.read()


db = sqlite3.connect(DB_NAME)
db.executescript(scripts)
db.commit()

print('database initialized.')