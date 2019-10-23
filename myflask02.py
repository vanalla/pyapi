#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hola_mundo():
    return "Hello World"
@app.route("/hello/<name>")
def hello(name):
    return "Hello {}".format(name)

if __name__ == "__main__" :
    app.run(port= 5006)
