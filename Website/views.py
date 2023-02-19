from flask import Blueprint, render_template, request

views = Blueprint('views', __name__)
error = Blueprint("error", __name__)

@views.route('/')
def home():
    return render_template("Search.html")

@error.route('/error')
def home():
    return render_template("error.html")