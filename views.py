from flask import Blueprint, render_template, redirect, url_for

views = Blueprint(__name__, "views")

@views.route("/")
@views.route("/home")
def home():
    return render_template("home.html")

@views.route("/estimator")
def estimator():
    return render_template("estimator.html")
