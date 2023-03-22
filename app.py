import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome to Python App!"

@app.route('/name')
def name():
    return 'Hi, I am Sandip Chatterjee'

@app.route('/age')
def age():
    return '27'

@app.route('/about')
def about():
    return 'I am good, how about you?'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
