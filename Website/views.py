from flask import Blueprint, render_template, request
from flask import Flask, redirect
from scrape import scraper

views = Blueprint('views', __name__)
term = ""
definition = ""
example = ""

@views.route('/', methods=['POST','GET'])
def home():
    if request.method == 'POST':
        search_term = request.form['q']
        global term
        global definition
        global example
        term = search_term
        list_scrape = scraper(term)
        definition = list_scrape[0]
        example = list_scrape[1]
        return redirect('/result')
    else:
        print("WHAT THE FUCK " + request.method)
    return render_template("Search.html")

@views.route('/error', methods=['GET', 'POST'])
def error():
    return render_template("error.html")

@views.route('/result', methods=['GET', 'POST'])
def result():
    global term
    global definition
    global example
    return render_template("definition.html", search=term, definition=definition, example=example)