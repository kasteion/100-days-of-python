from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)


@app.route("/")
def home():
    current_year = datetime.now().year
    random_number = random.randint(1, 10)
    return render_template("index.html", num=random_number, year=current_year)


def get_gender(name: str):
    parameters = {
        "name": name
    }
    response = requests.get("https://api.genderize.io/", params=parameters)
    response.raise_for_status()
    data = response.json()
    return data["gender"]


def get_age(name: str):
    parameters = {
        "name": name
    }
    response = requests.get("https://api.agify.io/", params=parameters)
    response.raise_for_status()
    data = response.json()
    return data["age"]


@app.route("/guess/<name>")
def guess(name: str):
    gender = get_gender(name)
    age = get_age(name)
    return render_template("guess.html", name=name.title(), gender=gender, age=age)


def get_blogs():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    response.raise_for_status()
    return response.json()


@app.route("/blog")
def blog_page():
    blogs = get_blogs()
    return render_template("blog.html", blogs=blogs)


if __name__ == "__main__":
    app.run(debug=True)