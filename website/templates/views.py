from flask import Blueprint

#create blueprint
views = Blueprint('views', __name__)

#create a route for that blueprint
@views.route('/')
def home():
    return "<h1>Test</h1>"
