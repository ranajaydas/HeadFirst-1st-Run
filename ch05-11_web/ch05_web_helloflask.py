"""Basic flask application."""
from flask import Flask
from ch04_func_lettersearch import search4letters

app = Flask(__name__)  # Creates an instance of a flash object and assigns it to 'app'


@app.route('/')
# 'route' Decorator for app ('/' is the URL).
# Decorators can be applied to functions and classes
def hello() -> str:
    return 'Hello world from Flask!'


@app.route('/search4')
def do_search() -> str:
    phrase = 'Life, the universe and everything!'
    letters = 'eiru,!'
    return str(search4letters(phrase, letters))


app.run()
