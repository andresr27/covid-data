#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'This is my flask application!'

if __name__ == '__main__':
    app.run()
