from gevent import monkey; monkey.patch_all()
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
import gevent
from gevent.pywsgi import WSGIServer
from bapi_httpx import BAPIRequest
import json

app = Flask(__name__)
CORS(app, supports_credentials=True)

cookies = []
try:
    cookies = json.load(open('local/cookies.json', 'r'))
    print('Local saved cookies read.')
except Exception:
    pass

breq =  BAPIRequest(cookies)

def make_response_json(res_text):
    res = make_response(res_text)
    res.headers['Content-Type'] = 'application/json'
    return res

@app.route('/popular', methods=['GET'])
def get_popular():
    pn = request.args.get('pn', 1, type=int)
    ps = request.args.get('ps', 20, type=int)
    res_text = None
    def worker():
        nonlocal res_text
        try:
            res = breq.get_popular(pn, ps)
            res_text = res.content.decode()
        except Exception as e:
            print(e)
            res_text = r'{code: 1, message: "出错啦！"}'
    coro = gevent.spawn(worker)
    coro.join()
    return make_response_json(res_text)

@app.route('/cookies', methods=['GET', 'POST'])
def cookies_manage():
    if request.method == 'GET':
        op = request.args.get('operation')
        if op == 'refresh':
            breq.refresh_cookies()
        cookies_json = jsonify(breq.get_cookies())
        with open('local/cookies.json', 'wb') as f:
            f.write(cookies_json.data)
        return make_response_json(cookies_json)
    else:
        data = request.get_data()
        breq.set_cookies(json.loads(data))
        with open('local/cookies.json', 'wb') as f:
            f.write(data)
        return make_response_json(r'{code: 0, message: "保存成功！"}')

@app.route('/message/replytome', methods=['GET'])
def replytome():
    cur_id = request.args.get('id')
    cur_time = request.args.get('time')
    cursor = {}
    if cur_id is not None and cur_time is not None:
        cursor['id'] = cur_id
        cursor['reply_time'] = cur_time
    res_text = None
    def worker():
        nonlocal res_text
        try:
            res = breq.get_reply_to_me(cursor)
            res_text = res.content.decode()
        except Exception as e:
            print(e)
            res_text = r'{code: 1, message: "出错啦！"}'
    coro = gevent.spawn(worker)
    coro.join()
    return make_response_json(res_text)

@app.route('/myinfo', methods=['GET'])
def myinfo():
    res_text = None
    def worker():
        nonlocal res_text
        try:
            res = breq.get_my_info()
            res_text = res.content.decode()
        except Exception as e:
            print(e)
            res_text = r'{code: 1, message: "出错啦！"}'
    coro = gevent.spawn(worker)
    coro.join()
    return make_response_json(res_text)

@app.route('/test', methods=['GET'])
def test():
    return r'{code: 0, message: "成功连接到后端！"}'

@app.route('/message/approvaltome', methods=['GET'])
def approvaltome():
    cur_id = request.args.get('id')
    cur_time = request.args.get('time')
    cursor = {}
    if cur_id is not None and cur_time is not None:
        cursor['id'] = cur_id
        cursor['like_time'] = cur_time
    res_text = None
    def worker():
        nonlocal res_text
        try:
            res = breq.get_approval_to_me(cursor)
            res_text = res.content.decode()
        except Exception as e:
            print(e)
            res_text = r'{code: 1, message: "出错啦！"}'
    coro = gevent.spawn(worker)
    coro.join()
    return make_response_json(res_text)

@app.route('/dynamic', methods=['GET'])
def dynamic():
    dynamic_type = request.args.get('type')
    cur_page = request.args.get('page')
    cur_offset = request.args.get('offset')
    host_mid = request.args.get('host_mid')
    cursor = {
        'page': 1
    }
    if cur_page is not None and cur_offset is not None:
        cursor['page'] = cur_page
        cursor['offset'] = cur_offset
    res_text = None
    def worker():
        nonlocal res_text
        try:
            res = breq.get_dynamic(cursor, dynamic_type, host_mid)
            res_text = res.content.decode()
        except Exception as e:
            print(e)
            res_text = r'{code: 1, message: "出错啦！"}'
    coro = gevent.spawn(worker)
    coro.join()
    return make_response_json(res_text)

@app.route('/portal', methods=['GET'])
def portal():
    res_text = None
    def worker():
        nonlocal res_text
        try:
            res = breq.get_portal()
            res_text = res.content.decode()
        except Exception as e:
            print(e)
            res_text = r'{code: 1, message: "出错啦！"}'
    coro = gevent.spawn(worker)
    coro.join()
    return make_response_json(res_text)

if __name__ == '__main__':
    socket = ('127.0.0.1', 5174)
    server = WSGIServer(socket, app)
    print(f'Server is running on http://{socket[0]}:{socket[1]}')
    server.serve_forever()
