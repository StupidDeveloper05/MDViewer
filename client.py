import socketio
import time


sio = socketio.Client()
sio.connect("http://localhost:5000")

KEY = "cogIDWPk_og-Z-Q49yfKAg"

data = dict()
data["key"] = KEY
data["uuid"] = "uuidTest"

with open("user.txt", "r", encoding="utf-8") as file:
    data["msg"] = file.read()
    data["type"] = "user"
    data["status"] = "start"
    sio.send(data)

data = dict()
data["key"] = KEY
data["uuid"] = "uuidTest"

status = "start"
md = ""
with open("test.md", "r", encoding="utf-8") as file:
    for line in file:
        for word in line:
            data["msg"] = md + word
            data["type"] = "assistant"
            data["status"] = status
            md = data["msg"]
            status = "running"
            sio.send(data)
        #time.sleep(0.1)