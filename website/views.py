from flask import Blueprint, render_template

#create/set-up a blueprint
views = Blueprint('views', __name__)

#create a route for that blueprint
@views.route('/')
def home():
    return render_template("home.html")
