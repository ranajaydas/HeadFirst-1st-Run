"""Letter search for a phrase using a Flask webapp, SQL DB and a Context Manager. WHAAAAAT!"""
from flask import Flask, render_template, request, escape
from ch04_func_lettersearch import search4letters
import mysql.connector

app = Flask(__name__)                                 # Creates an instance of a flask object and assigns it to 'app'


# 'route' Decorator for app ('/' and '/entry' are the URLs).
# Decorators can be applied to functions and classes
@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!'     # Variables inside the html rendered
                           )


"""The context management protocol sounds intimidating and scary, but it’s actually
quite simple. It dictates that any class you create must define at least two magic
methods: __enter__ and __exit__. This is the protocol. When you adhere to the
protocol, your class can hook into the 'with' statement.

If you create a class that defines __enter__ and __exit__, the class is
automatically regarded as a context manager by the interpreter :D :D :D """


def log_request(req: 'flask_request', res: str) -> None:
    dbconfig = {'host': 'localhost',
                'user': 'lettersearch',
                'password': 'lettersearchpassword',
                'database': 'lettersearchlogDB'}

    conn = mysql.connector.connect(**dbconfig)      # ** unpacks the dictionary object, dbconfig
    cursor = conn.cursor()                          # Creates a cursor for MySQL. Think of it as mysql>_ in cmd

    # All of the above is setup code
    _SQL = """insert into log
              (phrase, letters, ip, browser_string, results)
              values
              (%s, %s, %s, %s, %s)"""
    cursor.execute(_SQL, (req.form['phrase'],       # Sends an execute command to the MySQL cursor
                          req.form['letters'],
                          req.remote_addr,
                          req.user_agent.browser,
                          res)
                   )
    # All of the below is tear-down code. Hmmm...if only there was a better way to do this...

    conn.commit()                                   # Forcibly commits any inserts to the log
    cursor.close()                                  # Closes the cursor
    conn.close()                                    # Closes the connection to MySQL


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

    # render_template is a handy Jinja2 function we imported above
    return render_template('results.html',
                           the_title='Here are your results:',                   # Variables inside the html rendered
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results,
                           )


if __name__ == '__main__':
    app.run(debug=True)
