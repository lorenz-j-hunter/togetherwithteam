from flask import Flask, render_template, request

app = Flask(__name__)

app.route("/")
def index():
    return render_template("index.html")

app.route("/private")
def private():
    return render_template("private.html")