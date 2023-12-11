from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField, RadioField, DateField, Field
from wtforms.validators import Email, InputRequired, DataRequired, Length, Regexp, EqualTo


class RegisterForm(FlaskForm):
    first_name = StringField("First name", validators=[DataRequired(), Regexp("[A-Z]+[a-z]{2,24}")])
    last_name = StringField("Last name", validators=[DataRequired(), Regexp("[A-Z]+[a-z]{2,24}")])
    email = EmailField("Email: ", validators=[DataRequired()])
    gender = RadioField("Gender: ", choices=[("male", "male"), ("female", "female")])
    birthday = DateField("Birthday: ")
    address = StringField("Address: ")
    username = StringField("Username: ", validators=[Regexp("[a-zA-Z.-_*$!0-9]{4,24}")])
    password = PasswordField("Password: ", validators=[DataRequired(), Length(4, 28)])
    password_repeat = PasswordField("Password: ", validators=[DataRequired(), Length(4, 28), EqualTo("password")])
    phone_number = StringField("Tel: ", validators=[DataRequired(), Regexp("[0-9]{8}")])
    terms_conditions = BooleanField("Terms&Conditions", default=False, validators=[DataRequired()])
    submit = SubmitField("Sign-up")


class LoginForm(FlaskForm):
    username = StringField("Login: ", validators=[DataRequired(), Regexp("[a-zA-Z.-_*$!]{8,24}")])
    password = PasswordField("Password: ", validators=[DataRequired(), Length(4, 28)])
    rememberme = BooleanField("Remember me", default=False)
    submit = SubmitField("Login")

