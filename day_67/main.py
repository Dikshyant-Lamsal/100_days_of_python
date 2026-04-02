from flask import Flask, redirect, render_template, request
from flask_bootstrap import Bootstrap5, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


COFFEE_CHOICES = [
    ("✘", "✘"),
    ("☕", "☕"),
    ("☕☕", "☕☕"),
    ("☕☕☕", "☕☕☕"),
    ("☕☕☕☕", "☕☕☕☕"),
    ("☕☕☕☕☕", "☕☕☕☕☕"),
]

WIFI_CHOICES = [
    ("✘", "✘"),
    ("💪", "💪"),
    ("💪💪", "💪💪"),
    ("💪💪💪", "💪💪💪"),
    ("💪💪💪💪", "💪💪💪💪"),
    ("💪💪💪💪💪", "💪💪💪💪💪"),
]

POWER_CHOICES = [
    ("✘", "✘"),
    ("🔌", "🔌"),
    ("🔌🔌", "🔌🔌"),
    ("🔌🔌🔌", "🔌🔌🔌"),
    ("🔌🔌🔌🔌", "🔌🔌🔌🔌"),
    ("🔌🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"),
]

class CafeForm(FlaskForm):
    cafename     = StringField(label='Cafe Name',     validators=[DataRequired(), Length(min=4, max=25)])
    location     = StringField(label='Location URL',  validators=[DataRequired(), URL()])
    open_time    = StringField(label='Open Time',     validators=[DataRequired(), Length(min=4, max=25)])
    close_time   = StringField(label='Close Time',    validators=[DataRequired(), Length(min=4, max=25)])
    coffee_rating = SelectField(label='Coffee Rating', choices=COFFEE_CHOICES, validators=[DataRequired()])
    wifi_rating   = SelectField(label='Wifi Rating',   choices=WIFI_CHOICES,   validators=[DataRequired()])
    power_rating  = SelectField(label='Power Outlet',  choices=POWER_CHOICES,  validators=[DataRequired()])
    submit        = SubmitField(label='Submit')



@app.route("/",methods=["GET"])
def home():
    return render_template("index.html")


@app.route('/add',methods=["GET","POST"])
def add_cafe():
    form = CafeForm()
    if request.method=="POST" and form.validate_on_submit():
        with open('cafe-data.csv', 'a', newline='', encoding='utf-8') as csv_file:
            csv_file.write(f"\n{form.cafename.data},"
                           f"{form.location.data},"
                           f"{form.open_time.data},"
                           f"{form.close_time.data},"
                           f"{form.coffee_rating.data},"
                           f"{form.wifi_rating.data},"
                           f"{form.power_rating.data}")
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes', methods=["GET"])
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.DictReader(csv_file)
        list_of_rows = list(csv_data)
    return render_template('cafes.html', cafes=list_of_rows)

if __name__ == '__main__':
    app.run(debug=True)
