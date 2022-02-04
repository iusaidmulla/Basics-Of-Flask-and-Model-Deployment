import pandas as pd
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hey everyone, what's up..!!<h1>"

if __name__ == '__main__':
    app.run(debug = True) # debug is for immediate reflection on website
