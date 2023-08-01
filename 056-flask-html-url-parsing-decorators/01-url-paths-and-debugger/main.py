from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello world!"

# /greet/john
@app.route("/greet/<username>")
def greet_username(username):
    return f"Hello {username}"


# /path/john/doe
@app.route("/path/<path:username>")
def greet_path(username):
    return f"Hello {username}"


# /greet/john/1
@app.route("/greet/<username>/<int:age>")
def greet_username_age(username, age):
    return f"Hello {username} of {age} years old"


if __name__ == "__main__":
    # To turn on debug mode
    app.run(debug=True)
