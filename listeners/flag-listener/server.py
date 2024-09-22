import requests
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    flag = request.args.get("flag")
    real_flag = "GEMASTIK{" + flag[len("GEMASTIK"):] + "}"
    requests.post("http://localhost:8000/api/post_flags", headers={
        "Authorization": "insert password here",
    }, json=[
        {
            "flag": real_flag,
            "team": "*",
            "sploit": "Listener Server"
        }
    ])
    print(real_flag)
    return real_flag

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5333)
