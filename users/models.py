from flask import current_app
from flask_login import UserMixin
from sqlalchemy import Integer, Column, String
from werkzeug.security import generate_password_hash, check_password_hash

from databases import Base


class User(UserMixin, Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(100), key='email', unique=True)
    password = Column(String(256), key='password')
    name = Column(String(50), key='name')
    tel = Column(String(20), key='tel')
    mobile = Column(String(20), key='mobile')

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