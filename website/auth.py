from flask import Blueprint

#set-up a blueprint
auth = Blueprint('auth', __name__)

#setting up routes
@auth.route('/login')
def login():
    return "<p>login</p>"

@auth.route('logout')
def logout():
    return "<p>logout</p>"

@auth.route('signup')
def signup():
    return "<p>signup</p>"