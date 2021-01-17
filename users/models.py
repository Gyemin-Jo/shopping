from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash

from app import db


class User(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    email = db.Column(db.String(100), key='email', unique=True)
    password = db.Column(db.String(256), key='password')
    name = db.Column(db.String(50), key='name')
    tel = db.Column(db.String(20), key='tel')
    mobile = db.Column(db.String(20), key='mobile')

    def __unicode__(self):
        return self.email

    def __init__(self, *args, **kwargs):
        password = kwargs.pop('password', None)
        super(User, self).__init__(*args, **kwargs)
        if password:
            self.set_password(password)

    def set_password(self, password):
        self.password = generate_password_hash(
            password, method=current_app.config['PROJECT_PASSWORD_HASH_METHOD']
        )

    def check_password(self, password):
        return check_password_hash(self.password, password)