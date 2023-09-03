import time
from flask import Flask, request, redirect, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def validate_filename(filename: str):
    banned = ['..', '/', '~']
    for substring in banned:
        if substring in filename:
            return False
    return True

@app.route('/')
def get_index():
    return 'use static', 200
    
@app.route('/error')
def get_error():
    time.sleep(5)
    return 'Error', 404

@app.route('/static/<filename>')
def get_static(filename):
    if not validate_filename(filename):
        return 'Invalid filename', 400
    with open('static/' + filename, 'r') as file:
        content = file.read()
    return content, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    