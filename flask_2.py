import pandas as pd
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hey everyone<h1>"
    return "<a href=https://www.w3schools.com>This is a link<a>"

@app.route('/about')
def about():
    return "<h1>we are the tech comapny<h1>"

@app.route('/contactus')
def contactus():
    return "<h1>office : +91-7350939560<h1>"
if __name__ == '__main__':
    app.run(debug = True)
