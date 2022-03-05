#import statements
from flask import Flask, render_template, redirect, session
from flask_session import Session
from user import routes

#app configuration
app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#landing page
@app.route("/")
def landing():
    return render_template('landing.html')

#login page
@app.route("/login/")
def login_page():
    return render_template('login.html')

#about page -- Source code
@app.route("/about/")
def about():
    return redirect("https://github.com/adityapatkar/covid-detection")

#main app
@app.route("/dashboard/")
def dashboard():
    return redirect("https://diagnose-aditya.herokuapp.com/")

#signup page
@app.route("/signup/")
def home():
    return render_template('home.html')

#iframe page
@app.route("/diagnose/")
def mainapp():
    if not session.get("email"):
        return redirect("/login/")
    return render_template('mainapp.html')

#logout functionality -- TODO
@app.route("/logout/")
def logout():
    session["email"] = None
    return redirect("/")