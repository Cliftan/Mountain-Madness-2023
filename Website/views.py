from flask import Blueprint, render_template, request
from flask import Flask, redirect
from scrape import scraper

views = Blueprint('views', __name__)
error = Blueprint("error", __name__)
result = Blueprint("result", __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        search_term = request.form.get('q')
        list_of_result = scraper(search_term)
        definition = list_of_result[0]
        example = list_of_result
        if definition == 0:
            return redirect("/error", code=302)
    return render_template("Search.html")

@error.route('/error', methods=['GET', 'POST'])
def home():
    return render_template("error.html")

@result.route('/result', methods=['GET', 'POST'])
def home():
    return render_template("definition.html")