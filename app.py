import hmac
import sys
from hashlib import sha1
from time import time
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

if len(sys.argv) < 3:
    print 'please provide cf_path and tempurl-key'
    sys.exit(1)

cf_path = sys.argv[1]
key = sys.argv[2]
target = cf_path.split('clouddrive.com', 1)[1]

def _get_signature(path, max_count=10, redirect='',
                   max_size=104857600, ttl=600):
    expires = int(time() + ttl)
    hmac_body = '%s\n%s\n%s\n%s\n%s' % (path, redirect, max_size,
                                        max_count, expires)
    data = {'cf_path': cf_path, 'path': path,
            'max_count': max_count, 'max_size': max_size,
            'redirect': redirect, 'expires': expires, 'hmac': hmac.new(key, hmac_body, sha1).hexdigest()}
    return data

@app.route("/signature")
def signature():
    return jsonify(_get_signature(cf_path=target))

@app.route("/dropzone")
def dropzone():
    return render_template('dropzone.html', fp=_get_signature(path=target))

@app.route("/")
def hello():
    return "go to /dropzone"

if __name__ == "__main__":
    app.run(debug=True)
