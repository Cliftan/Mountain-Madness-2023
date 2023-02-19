from flask import Blueprint, render_template, request
from flask import Flask

views = Blueprint('views', __name__)
error = Blueprint("error", __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        search_term = request.form.get('q')
            
        Flask.redirect(Flask.url_for())
    return render_template("Search.html")

@error.route('/error')
def home():
    return render_template("error.html")