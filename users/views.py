from flask import render_template, request, flash, Flask
from manage import app
from app import app, db, Session
from users.forms import LoginForm, RegisterForm
from users.models import User
from flask_bcrypt import Bcrypt
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

@app.route('/signUp', methods=['GET', 'POST'])
def signUp():

    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    repeatpassword = request.form['repeatpassword']
    tel = request.form['tel']
    mobile = request.form['mobile']

    user = User(name = name, email=email, password=password, tel=tel, mobile =mobile)

    db.session.add(user)
    db.session.commit()

    flash("회원가입 완료")
    return render_template('admin/users/login.html')

@app.route('/access', methods=['GET', 'POST'])
def access():
    form = LoginForm()

    email = request.form['email']
    password = request.form['password']

    print(email, password)
    return render_template('admin/users/product.html')