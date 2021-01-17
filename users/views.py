from flask import render_template, request

from manage import app
from users.forms import LoginForm, RegisterForm


# 로그인
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    context = {}

    return render_template('admin/users/login.html', context=context, form=form)

# 회원가입
@app.route('/register', methods=['GET', 'POST'])
def register():
    context = request.get_json()
    form = RegisterForm()
    return render_template('admin/users/register.html', form=form)