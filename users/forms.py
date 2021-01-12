from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, HiddenField, ValidationError


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
            form.user = db_session.query(User).filter(User.email == email).one()
        except:
            raise ValidationError(u'Login not found.')

    def validate_password(form, field):
        password = field.data
        if form.user:
            if not form.user.check_password(password):
                raise ValidationError(u'Incorrect password.')