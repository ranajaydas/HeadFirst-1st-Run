"""Letter search for a phrase using a Flask webapp"""
from flask import Flask, render_template, request
from ch04_func_lettersearch import search4letters

app = Flask(__name__)                                 # Creates an instance of a flask object and assigns it to 'app'


# 'route' Decorator for app ('/' is the URL).
# Decorators can be applied to functions and classes
@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!'     # variables inside the html rendered
                           )


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']                   # Refer to input name='phrase' in entry.html
    letters = request.form['letters']                 # Refer to input name='letters' in entry.html
    results = str(search4letters(phrase, letters))
    return render_template('results.html',
                           the_title='Here are your results:',                   # variables inside the html rendered
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results,
                           )


if __name__ == '__main__':
    app.run(debug=True)
