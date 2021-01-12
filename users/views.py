from flask import Blueprint, render_template, request

from users.forms import LoginForm, RegisterForm

users_app = Blueprint('users_app', __name__)


# 로그인
@users_app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    context = {}

    return render_template('admin/users/login.html', context=context, form=form)


# 회원가입
@users_app.route('/register', methods=['GET', 'POST'])
def register():
    context = request.get_json()
    form = RegisterForm()
    print(context)
    return render_template('admin/users/register.html', form=form)
