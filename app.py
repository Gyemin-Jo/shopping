from flask import Flask
from flask_restful import Api
from flask_wtf import CSRFProtect

from functions import number_format, date_format

app = Flask(__name__)
api = Api(app)

app.jinja_env.filters['number_format'] = number_format
app.jinja_env.filters['date_format'] = date_format


def create_app(config_filename, env=None):
    csrf = CSRFProtect(app)
    csrf.init_app(app)

    app.config.from_object(config_filename)

    return app