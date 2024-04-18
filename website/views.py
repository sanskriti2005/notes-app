from flask import Blueprint

#create/set-up a blueprint
views = Blueprint('views', __name__)

#create a route for that blueprint
@views.route('/')
def home():
    return "<h1>Test</h1>"
