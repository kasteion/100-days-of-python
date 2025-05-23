from flask import Flask, render_template
import requests

app = Flask(__name__)


all_posts = requests.get("https://api.npoint.io/db374ea0d0ef301a8da2").json()


@app.route("/")
def home_page():
    return render_template("index.html", posts = all_posts)


@app.route("/about")
def about_page():
    return render_template("about.html", route="about")


@app.route("/contact")
def contact_page():
    return render_template("contact.html", route="contact")


@app.route("/posts/<int:post_id>")
def post_page(post_id):
    filtered = filter(lambda post: post["id"] == post_id, all_posts)
    return render_template("post.html", route="post", post=list(filtered)[0])


if __name__ == "__main__":
    app.run(debug=True)
