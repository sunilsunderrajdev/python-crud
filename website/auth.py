from flask import Blueprint, render_template, request, flash, jsonify

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<h1>Hello World SSR Logout</h1>"

@auth.route('/sign-up')
def signup():
    return render_template("sign-up.html")
