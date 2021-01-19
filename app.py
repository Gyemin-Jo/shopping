from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from sqlalchemy import create_engine
from functions import number_format, date_format
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
api = Api(app)

app.jinja_env.filters['number_format'] = number_format
app.jinja_env.filters['date_format'] = date_format

app.config.from_object('settings')
db = SQLAlchemy(app)
engine = create_engine('mysql://roote@localhost/admin?charset=utf8', echo=True)
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)

def create_app(env=None):
    csrf = CSRFProtect(app)
    csrf.init_app(app)
    CORS(app)

    return app


