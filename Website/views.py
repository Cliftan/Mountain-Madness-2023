from flask import Blueprint, render_template, request
from flask import redirect
from api import defineWord

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
        list_scrape = defineWord(term)
        if list_scrape == 0:
            return redirect('/error')
        definition = list_scrape[0]
        example = list_scrape[1]
        return redirect('/result')
    return render_template("Search.html")

@views.route('/error', methods=['GET', 'POST'])
def error():
    global term
    return render_template("error.html", term=term)

@views.route('/result', methods=['GET', 'POST'])
def result():
    global term
    global definition
    global example
    return render_template("definition.html", search=term, definition=definition, example=example)