import requests
from flask import Flask, request
from flask_cors import CORS

FARMER_URL = "http://localhost:8000"
FARMER_PASSWORD = "insert password here"

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    flag = request.args.get("flag")
    real_flag = "GEMASTIK{" + flag[len("GEMASTIK"):] + "}"
    requests.post(f"{FARMER_URL}/api/post_flags", headers={
        "Authorization": FARMER_PASSWORD,
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
