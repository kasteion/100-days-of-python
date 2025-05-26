from flask_wtf import FlaskForm
# pip install email_validator
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    email = EmailField(label="Email:", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password:", validators=[DataRequired()])
    submit = SubmitField(label="Log In")
