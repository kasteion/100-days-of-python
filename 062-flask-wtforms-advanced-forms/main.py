from flask import Flask, render_template
# pip install Flask-WTF
from login_form import LoginForm
# pip install bootstrap-flask
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.secret_key = "VdZatWDHGAuKU5ixMOjf8Fs7cPzJrYge"
bootstrap = Bootstrap5(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    # If the result of validate on submit is true it means the form was submitted, so a post request
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
