from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, HiddenField, ValidationError

from users.models import User


class LoginForm(FlaskForm):
    user = None

    email = StringField(
    )

    password = PasswordField(
    )

    next = HiddenField()

    def validate_email(form, field):
        email = field.data
        try:
            form.user = User.query.get(email=email)
        except:
            raise ValidationError(u'Login not found.')

    def validate_password(form, field):
        password = field.data
        if form.user:
            if not form.user.check_password(password):
                raise ValidationError(u'Incorrect password.')


class RegisterForm(FlaskForm):
    user = None
    name = StringField()
    email = StringField()
    password = PasswordField()
    repeatpassword = PasswordField()
    phone = StringField()
    tel = StringField()
