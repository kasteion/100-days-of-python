from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
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

all_books = []

class BookForm(FlaskForm):
    book_name = StringField('Book Name', validators=[DataRequired()])
    book_author = StringField('Book Author', validators=[DataRequired()])
    rating = StringField('Rating', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/')
def home():
    return render_template('index.html', books = all_books)


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = BookForm()
    if form.validate_on_submit():
        data = {
            'title': form.book_name.data,
            'author': form.book_author.data,
            'rating': form.rating.data,
        }
        all_books.append(data)
        return redirect('/')
    return render_template('add.html', form=form)



if __name__ == "__main__":
    app.run(debug=True)

