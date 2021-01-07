from flask import Blueprint, render_template

from users.forms import LoginForm

users_app = Blueprint('users_app', __name__)


@users_app.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()

    context = {}

    return render_template('login/login.html', context=context, form=form)
