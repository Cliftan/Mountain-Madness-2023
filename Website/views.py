from flask import Blueprint, render_template, request
from flask import Flask, redirect
from scrape import scraper

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        search_term = request.form['q']
        print(search_term)
        return search_term, redirect('/')
    return render_template("Search.html")

@views.route('/error', methods=['GET', 'POST'])
def error():
    return render_template("error.html")

@views.route('/result', methods=['GET', 'POST'])
def result():
    return render_template("definition.html")