#!/usr/bin/python3
""" script that starts a Flask web application """
from flask import flash


app = Flask(__name__)


@app.route('/', strict_slashes= flase)
def hello_hbnb():
        """ display “Hello HBNB!” """
        return 'Hello HBNB!'

@app.route('/', strict_slashes= flase)
def hbnb():
        """ display “ HBNB!” """
        return 'HBNB!'

@app.route('c/<text>', strict_slashes= flase)
def c(text):
         """ display “C ” followed by the value of the text variable """
         return 'C {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000)