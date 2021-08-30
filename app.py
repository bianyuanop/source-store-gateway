import os
import json
from sqlite3.dbapi2 import Cursor
from flask import Flask, redirect
from flask_cors import CORS
import sqlite3
import util

from werkzeug.datastructures import ContentSecurityPolicy

app = Flask(__name__)
CORS(app)

HOSTS = {
    'v1': 'http://localhost:8080'
}

PARAM = {
    'commody': '/#/query/',
}

@app.route('/count', methods=['GET'])
def counter():
    db = sqlite3.connect('./counter.db')
    cursor = db.cursor()
    query_res = cursor.execute('SELECT count FROM counter WHERE id=1').fetchone()
    print(query_res[0])

    return json.dumps({
        'count': query_res[0]
    })

@app.route('/gateway/<encoded_sig>', methods=['GET'])
def gateway(encoded_sig):

    directTo = util.decrypt(encoded_sig, util.secret_key)

    db = sqlite3.connect('./counter.db')
    cursor = db.cursor()
    res = cursor.execute('UPDATE counter SET count=count+1 WHERE id=1')
    db.commit()

    redirect(directTo, 302)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)