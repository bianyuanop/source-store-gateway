import json
from sqlite3.dbapi2 import Cursor
from flask import Flask, redirect, request
from flask_cors import CORS
import sqlite3
import util

app = Flask(__name__)
CORS(app)

HOSTS = {
    'v1': 'https://hoir7-dyaaa-aaaah-aaqna-cai.raw.ic0.app'
}

PARAM = {
    'query': '#/query',
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

@app.route('/gateway', methods=['GET'])
def gateway():

    encoded_sig = request.args.get('sig')
    print(encoded_sig)

    redirect_template = '{0}/{1}/{2}'
    try:
        info = util.decrypt(encoded_sig.encode('ascii'), util.secret_key)
        info = info.decode('ascii')
        info = json.loads(info)

        version = info['version']
        param = info['param']
        arg = info['arg']

        print(version, param, arg)

        if version not in HOSTS.keys():
            return json.dumps({
                'msg': 'version not exists'
            })
        
        if param not in PARAM.keys():
            return json.dumps({
                'msg': 'param not correct'
            })

        host = HOSTS[version]
        method = PARAM[param]

        directTo = redirect_template.format(host, method, arg)

    except Exception as e:
        return json.dumps({
            'msg': str(e)
        })

    db = sqlite3.connect('./counter.db')
    cursor = db.cursor()
    res = cursor.execute('UPDATE counter SET count=count+1 WHERE id=1')
    db.commit()

    return redirect(directTo, 302)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)