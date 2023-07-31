# Install Flask:
# https://flask.palletsprojects.com/en/2.3.x/installation/

from flask import Flask # pip install Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/bye")
def bye():
    return "<p>Bye</p>"

# Run:
# flask --app hello run


# __name__ and __main__ are special attributes built into python
if __name__ == "__main__":
    app.run()
