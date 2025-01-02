from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "<h1>Hello World SSR Login</h1>"

@auth.route('/logout')
def logout():
    return "<h1>Hello World SSR Logout</h1>"

@auth.route('/signup')
def signup():
    return "<h1>Hello World SSR Signup</h1>"
