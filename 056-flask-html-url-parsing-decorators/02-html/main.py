from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper_function():
        return f'<b>{function()}</b>'
    return wrapper_function


def make_emphasis(function):
    def wrapper_function():
        return f'<em>{function()}</em>'
    return wrapper_function


def make_underlined(function):
    def wrapper_function():
        return f'<u>{function()}</u>'
    return wrapper_function


@app.route("/")
def hello_world():
    return '<h1 style="text-align: center">Hello World!</h1>' \
           '<p>This is a paragraph</p>' \
           '<iframe src="https://giphy.com/embed/K1tgb1IUeBOgw" ' \
           'width="480" height="278" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>'


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye"


if __name__ == '__main__':
    app.run(debug=True)
