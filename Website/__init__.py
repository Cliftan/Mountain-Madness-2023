from flask import Flask
from .views import views, error, result

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'temporarypass'

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(error, url_prefix="/")
    app.register_blueprint(result, url_prefix="/")

    return app