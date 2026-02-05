from flask import Flask, render_template, request

app = Flask(__name__)

app.route("/")
def index():
    return render_template("index.html")

app.route("/private", methods=["GET"])
def private():
    user = request.args.get("username")
    password = request.args.get("password")
    return render_template("private.html", user=user, password=password)