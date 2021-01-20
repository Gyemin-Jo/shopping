from flask import current_app, render_template
from werkzeug.security import generate_password_hash, check_password_hash
from bcrypt import _bcrypt
from app import db

class User(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}
    name = db.Column(db.String(100), key = 'name', primary_key=True)
    email = db.Column(db.String(100), key='email', unique=True)
    password = db.Column(db.String(256), key='password')
    repeatpassword = db.Column(db.String(256), key='repeatpassword')
    phone = db.Column(db.String(20), key='phone')
    mobile = db.Column(db.String(20), key='mobile')