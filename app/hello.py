#!flask/bin/python
from flask import render_template
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('hello.html')
    
@app.route('/tesla')
def tesla():
    return 'Tesla data coming soon...';

if __name__ == '__main__':
    app.run(host='0.0.0.0')
