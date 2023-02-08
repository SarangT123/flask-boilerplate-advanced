from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,TextAreaField
from wtforms.validators import InputRequired, Length, ValidationError
from website.models import User
from flask import flash


class Register(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
        min=3, max=20)], render_kw={'placeholder': 'Username'})
    password = PasswordField(validators=[InputRequired(), Length(
        min=8, max=20)], render_kw={'placeholder': 'Password'})
    submit = SubmitField("Register")

    def validate_username(self, username):
        exist = User.query.filter_by(username=username.data).first()

        if exist:
            print("Username taken")
            flash("Username taken")
            raise ValidationError("Username taken")


class Login(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
        min=3, max=20)], render_kw={'placeholder': 'Username'})
    password = PasswordField(validators=[InputRequired(), Length(
        min=8, max=20)], render_kw={'placeholder': 'Password'})
    submit = SubmitField("Login")

class User_id_search(FlaskForm):
    user = StringField(validators=[InputRequired(), Length(
        min=3, max=20)], render_kw={'placeholder': 'Username'})
    submit = SubmitField("Search")

class Admin_requests(FlaskForm):
    reason = TextAreaField(validators=[InputRequired(), Length(min=10, max=1000)], render_kw={'placeholder': 'Reason in 1000 characters or less'})
    submit = SubmitField("Submit")
