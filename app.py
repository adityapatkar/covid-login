from flask import Flask, render_template, redirect

app = Flask(__name__)


#--- routes start ---
from user import routes

@app.route("/")
def landing():
    return render_template('landing.html')

@app.route("/login/")
def login_page():
    return render_template('login.html')

@app.route("/about/")
def about():
    return redirect("https://github.com/adityapatkar/covid-detection")

@app.route("/dashboard/")
def dashboard():
    return redirect("https://diagnose-aditya.herokuapp.com/")

@app.route("/signup/")
def home():
    return render_template('home.html')

@app.route("/diagnose/")
def mainapp():
    return render_template('mainapp.html')