from flask import Flask, render_template
import requests
from post import Post


app = Flask(__name__)


def get_posts():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    posts = [
        Post(post_id=post["id"], title=post["title"], subtitle=post["subtitle"], body=post["body"])
        for post in response.json()
    ]
    return posts


def get_post(blog_id):
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    data = [
        Post(post_id=post["id"], title=post["title"], subtitle=post["subtitle"], body=post["body"])
        for post in response.json()
        if post["id"] == 2
    ]
    return data[0]


@app.route('/')
def home():
    posts = get_posts()
    return render_template("index.html", posts=posts)


@app.route('/post/<int:blog_id>')
def post_page(blog_id):
    post = get_post(blog_id)
    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(port=8000, debug=True)