import secrets
from flask import Flask, render_template
from flask_socketio import SocketIO, send
from flask import request
import time

ACCESS_KEY = secrets.token_urlsafe(16);
print(f"ACCESS KEY is {ACCESS_KEY}")

app = Flask(__name__)
socket_io = SocketIO(app, cors_allowed_origins="*")

Cache = []
Data = dict()

@app.route('/')
def home():
    return '<h1>웹 마크다운 뷰어</h1>'

@app.route('/chat/<uuid>')
def chat_view(uuid):
    accessKey = request.args.get("key", "")
    if accessKey == ACCESS_KEY:
        return render_template("develope.html", 
                               Data=[] if Data.get(uuid) == None else Data[uuid], 
                               UUID=uuid)
    else:
        return "<h1>액세스 키가 유효하지 않습니다.</h1>"

@socket_io.on("message")
def request_io(msg):
    if msg["key"] == ACCESS_KEY:
        if msg['uuid'] not in Data:
            Data[msg['uuid']] = []
        if msg["status"] == "running":
            Data[msg['uuid']][-1] = (msg["type"], msg["msg"])
        else:
            Data[msg['uuid']].append((msg["type"], msg["msg"]))
        send(msg, broadcast=True)
    print(f"[{time.strftime('%Y.%m.%d %p %I:%M:%S')}] {msg['type'].upper()} : {msg['status']}")

if __name__ == "__main__":
    socket_io.run(app, debug=True)