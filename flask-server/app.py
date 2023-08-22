import time
from flask import Flask, request, redirect, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def get_csrf_html():
    return render_template('tbdxss.html'), 200
    
@app.route('/error')
def get_error():
    time.sleep(5000)
    return 'Error', 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    