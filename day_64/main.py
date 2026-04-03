from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, TextAreaField
from wtforms.validators import DataRequired
import requests


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
  pass

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie-collection.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)

class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year : Mapped[int] = mapped_column(Integer, nullable=False)
    description : Mapped[str] = mapped_column(String(250), nullable=False)
    rating : Mapped[float] = mapped_column(Float, nullable=False)
    review : Mapped[str] = mapped_column(String(1000), nullable=False)
    img_url : Mapped[str] = mapped_column(String(250), nullable=False) 
# CREATE TABLE
# with app.app_context():
#     db.create_all()
class AddForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    year = StringField("Movie Year", validators=[DataRequired()])
    description = TextAreaField("Movie Description", validators=[DataRequired()])  # changed
    rating = FloatField("Your Rating Out of 10 e.g. 7.5", validators=[DataRequired()])
    review = TextAreaField("Your Review", validators=[DataRequired()])  # optional: same for review
    img_url = StringField("Movie Image URL", validators=[DataRequired()])
    submit = SubmitField("Add Movie")
    
class EditForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    year = StringField("Movie Year", validators=[DataRequired()])
    description = TextAreaField("Movie Description", validators=[DataRequired()])  # changed
    rating = FloatField("Your Rating Out of 10 e.g. 7.5", validators=[DataRequired()])
    review = TextAreaField("Your Review", validators=[DataRequired()])  # optional: same for review
    img_url = StringField("Movie Image URL", validators=[DataRequired()])
    submit = SubmitField("Update Movie")
    
@app.route("/",methods=["GET", "POST"])
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = result.scalars()
    return render_template("index.html", movies=all_movies)

@app.route("/add", methods=["GET", "POST"])
def add():
    add_form = AddForm()
    if add_form.validate_on_submit():
        new_movie = Movie(
            title=add_form.title.data,
            year=int(add_form.year.data),
            description=add_form.description.data,
            rating=add_form.rating.data,
            review=add_form.review.data,
            img_url=add_form.img_url.data
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html", form=add_form)

@app.route("/edit/<int:movie_id>", methods=["GET", "POST"])
def edit(movie_id):
    movie = db.get_or_404(Movie, movie_id)
    edit_form = EditForm(obj=movie)
    if edit_form.validate_on_submit():
        movie.title = edit_form.title.data
        movie.year = int(edit_form.year.data)
        movie.description = edit_form.description.data
        movie.rating = edit_form.rating.data
        movie.review = edit_form.review.data
        movie.img_url = edit_form.img_url.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", form=edit_form, movie=movie)

@app.route("/delete/<int:movie_id>", methods=["GET", "POST"])
def delete(movie_id):
    movie = db.get_or_404(Movie, movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)