"""Another simple webapp to demo restricted login using sessions and this time...DECORATORS."""
from flask import Flask, session
from ch10_decor_checklogin import check_logged_in

app = Flask(__name__)
app.secret_key = 'ChoduChamaar'


@app.route('/')
def entry() -> str:
    return 'Welcome to this simple webapp!'


@app.route('/login')
def login() -> str:
    session['logged-in'] = True
    return 'You are now logged in!'


@app.route('/logout')
def logout() -> str:
    session.pop('logged-in')
    return 'Bye, mofo!'


@app.route('/page1')
@check_logged_in
def page1() -> str:
    """Now, adding in some extra login checking code or a function here
     would be a terrible way of doing things because the login check
     has nothing to do with the core functionality of this page.

     Instead, we use the check_logged_in decorator y'all!"""

    return 'You are in PAGE 1 now!'


@app.route('/page2')
@check_logged_in
def page2() -> str:
    return 'You are in PAGE 2 now!'


@app.route('/page3')
@check_logged_in
def page3() -> str:
    return 'You are in PAGE 3 now!'


if __name__ == '__main__':
    app.run(debug=True)
