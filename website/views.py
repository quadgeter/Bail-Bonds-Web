from flask import Flask, render_template, Blueprint
from Inmate import Inmate
from InmateDB import loadInmates

views = Blueprint("views", __name__)



@views.route('/')
def index():
    
    return render_template("login.html")

headings = ("First", "Last", "Id Number", "Court Date", "Bond Amount", "Bond Paid", "Charges", "Contact Name", "Contact Phone")
data = (
        ("Carl", "Johnson", "0001", "12/12/2023", 1200, 900, "Murder", "Sherice Johnson", "(980)-324-4356"),
        ("Joe", "Lewis", "0002", "10/22/2023", 2000, 890, "Theft", "Kyle Lewis", "(980)-234-3445"),
        ("Jarod", "Green", "0003", "11/29/2023", 1900, 700, "Robbery", "Taniyah Green", "(704)-123-4567") 
    )

@views.route("/info.html")
def info():
    return render_template("info.html", headings=headings, data=data)

@views.route("/settings.html")
def settings():
    return render_template("settings.html")

@views.route("/home.html")
def home():
    return render_template("home.html")