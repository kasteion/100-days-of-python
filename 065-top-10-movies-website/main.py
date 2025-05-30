from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, NumberRange
import requests
import os

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies-collection.db'
db.init_app(app)

TMDB_API_KEY = os.environ.get("TMDB_API_KEY")

# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[int] = mapped_column(Integer, nullable=False)
    review: Mapped[str] = mapped_column(String, nullable=False)
    img_url: Mapped[str] = mapped_column(String, nullable=False)

with app.app_context():
    db.create_all()
    # movie = Movie(
    #     title="Avatar The Way of Water",
    #     year=2022,
    #     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
    #     rating=7.3,
    #     ranking=9,
    #     review="I liked the water.",
    #     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
    # )
    # db.session.add(movie)
    # db.session.commit()

class CreateMovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')

class EditMovieForm(FlaskForm):
    rating = FloatField('Your Rating Out of 10 e.g. 7.5', validators=[DataRequired(), NumberRange(0, 10)])
    review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Done')

@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    movies = result.scalars().all()
    ordered_movies = [{ 'id': m.id, 'title': m.title, 'year': m.year, 'description': m.description, 'rating': m.rating, 'ranking': len(movies) - ind, 'review': m.review, 'img_url': m.img_url} for ind, m in enumerate(movies)]
    return render_template("index.html", movies = ordered_movies)

@app.route("/edit", methods=['GET', 'POST'])
def edit():
    form = EditMovieForm()
    id = request.args.get('id')
    movie = db.get_or_404(Movie, id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect('/')
    return render_template("edit.html", movie = movie, form = form)

@app.route("/delete")
def delete():
    id = request.args.get('id')
    movie = db.get_or_404(Movie, id)
    db.session.delete(movie)
    db.session.commit()
    return redirect("/")

@app.route("/add", methods=['GET', 'POST'])
def add():
    url = 'https://api.themoviedb.org/3'
    headers = {
        "accept": "application/json",
    }
    id = request.args.get('id')
    form = CreateMovieForm()
    if form.validate_on_submit(): 
        res = requests.get(f'{url}/search/movie?api_key={TMDB_API_KEY}&include_adult=false&language=en-US&page=1&query={form.title.data}', headers=headers)
        return render_template("select.html", movies = res.json()['results'])
    if id:
        res = requests.get(f'{url}/movie/{id}?api_key={TMDB_API_KEY}&language=en-US', headers=headers)
        data = res.json()
        # print(data['title'], str(data['release_date'])[:4], data['overview'], )
        movie = Movie(title=data['title'], year=int(data['release_date'][:4]), description=data['overview'], rating=data['vote_average'], ranking=0, review='', img_url=f"https://image.tmdb.org/t/p/w1280/{data['poster_path']}")
        db.session.add(movie)
        db.session.commit()
        return redirect(f"/edit?id={movie.id}")
    return render_template("add.html", form = form)

if __name__ == '__main__':
    app.run(debug=True)
