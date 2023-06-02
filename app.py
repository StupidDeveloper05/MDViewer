from flask import Flask, render_template, url_for
from flask_socketio import SocketIO, send
from flask_cors import CORS
import time

app = Flask(__name__)
socket_io = SocketIO(app, cors_allowed_origins="*")

Cache = []

@app.route('/')
def home():
    return render_template("develope.html", Cache=Cache)

@socket_io.on("message")
def request(msg):
    if msg["type"] == "backup":
        if msg["status"] == "running":
            Cache[-1] = (msg["owner"], msg["html"])
        else:
            Cache.append((msg["owner"], msg["html"]))
    else:
        send(msg, broadcast=True)
    print(f"[{time.strftime('%Y.%m.%d %p %I:%M:%S')}] {msg['type'].upper()} : {msg['status']}")

if __name__ == "__main__":
    socket_io.run(app, debug=True)    