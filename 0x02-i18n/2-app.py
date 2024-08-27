#!/usr/bin/env python3
"""
File: 2-app.py

A simple flask app with babel extension

Author: Malik Hussein
"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """
    Class for the Flask app's configuration.
    Used to configure Flask app's languages and timezone.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])

babel = Babel(app, locale_selector=get_locale)




@app.route('/')
def index():
    """
    Route for the homepage

    This route is configured to the '/' URL.
    It returns the rendered '0-index.html' template.
    """
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run()
