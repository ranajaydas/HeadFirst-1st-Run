"""Letter search for a phrase using a Flask webapp."""
from flask import Flask, render_template, request, escape
from ch04_func_lettersearch import search4letters

app = Flask(__name__)                                 # Creates an instance of a flask object and assigns it to 'app'


# 'route' Decorator for app ('/' is the URL).
# Decorators can be applied to functions and classes
@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!'     # Variables inside the html rendered
                           )


def log_request(req: 'flask_request', res: str) -> None:
    with open('lettersearch.log', 'a') as log_file:                             # Always open files with 'with open'
        print(req.form,
              req.remote_addr,
              req.user_agent,
              res,
              file=log_file,
              sep='|')


@app.route('/viewlog')
def view_the_log() -> 'html':
    contents = []
    with open('lettersearch.log') as log_file:
        for row in log_file:
            contents.append([])
            for item in row.split('|'):               # Split each row by the delimiter '|'
                contents[-1].append(escape(item))     # escape function deals with HTML tags like '<', '>' etc

    return render_template('viewlog.html',
                           the_title='Log of Letter Searches:',
                           the_row_titles=['Form Data', 'Remote Addr', 'User Agent', 'Results'],
                           the_data=contents)


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']                   # Refer to input name='phrase' in entry.html
    letters = request.form['letters']                 # Refer to input name='letters' in entry.html
    results = str(search4letters(phrase, letters))
    log_request(request, results)
    return render_template('results.html',
                           the_title='Here are your results:',                   # Variables inside the html rendered
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results,
                           )


if __name__ == '__main__':
    app.run(debug=True)
