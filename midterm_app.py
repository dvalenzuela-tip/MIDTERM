from flask import Flask 
from flask import request
from flask import render_template
from flask import redirect

midterm = Flask(__name__)

@midterm.route("/")
def main():
    return redirect("/login", code=302)

@midterm.route("/login")
def login():
    return render_template("login.html")

@midterm.route("/register")
def register():
    return render_template("register.html")

if __name__ == "__main__":
    midterm.run(host="0.0.0.0", port=5000)