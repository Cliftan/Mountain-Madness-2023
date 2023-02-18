from flask import Blueprint, render_template, request

views = Blueprint('views', __name__)

@views.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        search_term = request.form.get("search_term")
    return "<h1> Hi </h1>"