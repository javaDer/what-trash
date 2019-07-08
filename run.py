# -*- coding: utf-8 -*-
import json

from flask import Flask, request, make_response

import trash

global false, null, true
false = null = true = ""
app = Flask(__name__)


@app.route('/trash', methods=['GET'])
def what_trash():
    trashname = request.args.get('name')
    res = trash.trash(trashname)
    status = 0
    if '属于' in res:
        status = 1
    ans = {
        'status': status,
        'content': res
    }
    ans = make_response(json.dumps(ans))
    ans.headers['Access-Control-Allow-Origin'] = '*'
    ans.headers['Content-Type'] = 'application/json'
    return ans


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=1028)  # host='0.0.0.0', port=80,
