from flask import Flask, render_template, redirect, session
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

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
    if not session.get("email"):
        return redirect("/login/")
    return render_template('mainapp.html')

@app.route("/logout/")
def logout():
    session["email"] = None
    return redirect("/")