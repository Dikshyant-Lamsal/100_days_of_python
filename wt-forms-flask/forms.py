from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email(message='Invalid email address.'), Length(min=4, max=25)])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=4, max=25)])
    submit = SubmitField(label='Login')