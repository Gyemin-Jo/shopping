from flask import render_template, request

from manage import app
from app import app, db, session
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

@app.route('/signUp', methods=['GET', 'POST'])
def signUp():

    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    repeatpassword = request.form['repeatpassword']
    phone = request.form['phone']
    mobile = request.form['mobile']

    users = {'name': name,'email':email,'password':password,'repeatpassword':repeatpassword,'phone':phone,'mobile':mobile}

    print(users)

    session.add(users)
    session.commit()

    return render_template('admin/users/login.html')