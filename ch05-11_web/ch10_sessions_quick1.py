"""A simple program to demo browser sessions. Use 2 different browsers to test it."""
from flask import Flask, session

app = Flask(__name__)
app.secret_key = 'ChootPakodaIsAHardPassword'


@app.route('/setuser/<user>')        # The URL expects to be provided a value to assign to 'user'
def setuser(user: str) -> str:
    """By automatically setting a unique cookie within each browser, the webapp (thanks to
       session) maintains a browser-identifiable value of user for each browser."""

    session['user'] = user           # The value of 'user' is assigned to the 'user' key in the 'session' dictionary
    print(session)
    return 'User value set to: ' + session['user']


@app.route('/getuser')
def getuser() -> str:
    return 'User value is currently set to: ' + session['user']


if __name__ == '__main__':
    app.run(debug=True)
