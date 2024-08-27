#!/usr/bin/env python3
"""
File: 1-app.py

A simple flask app with babel extension

Author: Malik Hussein
"""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config():
    """
    Class for the Flask app's configuration.
    Used to configure Flask app's languages and timezone.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def index():
    """
    Route for the homepage

    This route is configured to the '/' URL.
    It returns the rendered '1-index.html' template.
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()
