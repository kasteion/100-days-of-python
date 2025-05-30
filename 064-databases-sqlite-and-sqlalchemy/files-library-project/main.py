from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, NumberRange

# SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
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

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-collection.db'
db.init_app(app)

class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

with app.app_context():
    db.create_all()
    # book = Book(id=1, title="Harry Potter", author="J.K. Rowling", rating=9.3)
    # db.session.add(book)
    # db.session.commit()

all_books = []

class BookForm(FlaskForm):
    book_name = StringField('Book Name', validators=[DataRequired()])
    book_author = StringField('Book Author', validators=[DataRequired()])
    rating = FloatField('Rating', validators=[DataRequired(), NumberRange(0, 10)])
    submit = SubmitField('Submit')

class UpdateRatingForm(FlaskForm):
    rating = FloatField('Rating', validators=[DataRequired(), NumberRange(0, 10)])
    submit = SubmitField('Change Rating')

@app.route('/')
def home():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars().all()
    return render_template('index.html', books = all_books)


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = BookForm()
    if form.validate_on_submit():
        # data = {
        #     'title': form.book_name.data,
        #     'author': form.book_author.data,
        #     'rating': form.rating.data,
        # }
        # all_books.append(data)
        book = Book(title=form.book_name.data, author=form.book_author.data, rating=float(form.rating.data))
        db.session.add(book)
        db.session.commit()
        return redirect('/')
    return render_template('add.html', form=form)

@app.route('/edit', methods=['GET', 'POST'])
def edit():
    form = UpdateRatingForm()
    id = request.args.get('id')
    book = db.session.execute(db.select(Book).where(Book.id == id)).scalar()
    if form.validate_on_submit():
        book.rating = float(form.rating.data)
        db.session.commit()
        return redirect('/')
    return render_template('edit.html', book=book, form=form)

@app.route('/delete')
def delete():
    id = request.args.get('id')
    book = db.get_or_404(Book, id)
    db.session.delete(book)
    db.session.commit()
    return redirect('/')




if __name__ == "__main__":
    app.run(debug=True)

