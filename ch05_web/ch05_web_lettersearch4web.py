"""Letter search for a phrase using a Flask webapp"""
from flask import Flask, render_template
from ch04_func_lettersearch import search4letters

app = Flask(__name__)                       # Creates an instance of a flash object and assigns it to 'app'


# 'route' Decorator for app ('/' is the URL).
# Decorators can be applied to functions and classes
@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!'
                           )


@app.route('/search4')
def do_search() -> 'html':
    phrase = 'Life, the universe and everything!'
    letters = 'eiru,!'
    return str(search4letters(phrase, letters))


app.run()
