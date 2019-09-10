"""Letter search for a phrase using a Flask webapp, SQL DB,
Context Manager, Decorators error handling AND threading. WHAAAAAT!"""

from flask import Flask, render_template, request, session
from ch04_func_lettersearch import search4letters
from ch09_ctxtmgr_DBcm import UseSQLDatabase, MySQLConnectionError, CredentialsError, SQLError
from ch10_decor_checklogin import check_logged_in
from threading import Thread

# copy_current_request_context ensures that the HTTP request that is active when a function
# is called remains active even when the function is subsequently executed in a thread.
from flask import copy_current_request_context


app = Flask(__name__)                                  # Creates an instance of a flask object and assigns it to 'app'
app.config['dbconfig'] = {'host': 'localhost',         # app.config is Flask's built-in configuration mechanism
                          'user': 'lettersearch',
                          'password': 'lettersearchpassword',
                          'database': 'lettersearchlogDB'}


# 'route' Decorator for app ('/' and '/entry' are the URLs).
# Decorators can be applied to functions and classes
@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    """Renders the entry page."""

    # render_template is a handy Jinja2 function we imported above
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!'     # Variables inside the html file
                           )


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    """Function that's called when the 'Do it' button is pressed."""
    phrase = request.form['phrase']                   # Refer to input name='phrase' in entry.html
    letters = request.form['letters']                 # Refer to input name='letters' in entry.html
    results = str(search4letters(phrase, letters))    # Custom module, search4letters, imported above

    """The context management protocol sounds intimidating and scary, but it’s actually
    quite simple. It dictates that any class you create must define at least two magic
    methods: __enter__ and __exit__. This is the protocol. When you adhere to the
    protocol, your class can hook into the 'with' statement.

    If you create a class that defines __enter__ and __exit__, the class is
    automatically regarded as a context manager by the interpreter :D :D :D """

    @copy_current_request_context                     # To handle threading
    def log_request(req: 'flask_request', res: str) -> None:
        """Logs any requests to a MySQL database."""
        import time  # TODO: REMOVE THIS LATER. ONLY ADDED TO DEMO THREADING
        time.sleep(15)  # TODO: REMOVE THIS LATER. ONLY ADDED TO DEMO THREADING

        # Use the with statement now that the context manager (UseSQLDatabase) is created!
        with UseSQLDatabase(app.config['dbconfig']) as cursor:
            _SQL = """insert into log
                      (phrase, letters, ip, browser_string, results)
                      values
                      (%s, %s, %s, %s, %s)"""
            cursor.execute(_SQL, (req.form['phrase'],  # Sends an execute command to the MySQL cursor
                                  req.form['letters'],
                                  req.remote_addr,
                                  req.user_agent.browser,
                                  res)
                           )

    try:
        t = Thread(target=log_request, args=(request, results))              # Function defined within this module
        t.start()
    except Exception as err:
        print('***** Logging failed with this error:', str(err))

    return render_template('results.html',
                           the_title='Here are your results:',
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results,
                           )


@app.route('/login')
def login() -> str:
    session['logged-in'] = True
    return 'You are now logged in!'


@app.route('/logout')
def logout() -> str:
    session.pop('logged-in')
    return 'Bye, mofo!'


@app.route('/viewlog')
@check_logged_in                                          # Custom made decorator to check if a user is logged in
def view_the_log() -> 'html':
    """View all logged requests in HTML."""
    try:
        # Another use of the context manager!
        with UseSQLDatabase(app.config['dbconfig']) as cursor:
            _SQL = """select id, ts, phrase, letters, ip, browser_string, results 
                      from log"""
            cursor.execute(_SQL)                          # Sends an execute command to the MySQL cursor
            contents = cursor.fetchall()                  # Fetches any results produced by the execute

        return render_template('viewlog.html',
                               the_title='Log of Letter Searches:',
                               the_row_titles=['id', 'Timestamp', 'Phrase', 'Letters', 'IP', 'Browser', 'Results'],
                               the_data=contents)

    except MySQLConnectionError as err:                   # Custom made Exception type imported above
        print('***** Is the database connected? Error:', err)
    except CredentialsError as err:                       # Custom made Exception type imported above
        print('***** Is the username/password correct? Error:', err)
    except SQLError as err:                               # Custom made Exception type imported above
        print('***** Is the query correct? Error:', err)
    except Exception as err:
        print('***** Something went wrong: ', err)
    return 'Error'


app.secret_key = 'ChootPakodaExtraordinaire'

if __name__ == '__main__':
    app.run(debug=True)
