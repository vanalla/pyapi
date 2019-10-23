#!/usr/bin/python3
from flask import Flask
from flask import redirect 
from flask import url_for 

app = Flask(__name__)

@app.route("/admin")
def hello_admin():
    return "Hello administrator"

@app.route("/guest/<guesty>")
def hello_guest(guesty):
    return "Hello {} Guest".format(guesty)

@app.route("/signin/<name>")
def signin(name):
    if name == "admin":
        return redirect(url_for("hello_admin"))
    else:
        return redirect(url_for("hello_guest", guesty = name))

if __name__ == "__main__": 
    app.run(port= 5006)
