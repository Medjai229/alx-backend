#!/usr/bin/env python3
"""
File: 3-app.py

A simple flask app with babel extension

Author: Malik Hussein
"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Class for the Flask app's configuration.
    Used to configure Flask app's languages and timezone.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    Return the best match for language based on the
    Accept-Language HTTP header sent by the client.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


# That code was written for flask-babel=2.0.0
# If you wanna use it for flask-babel=4.0.0
# Comment the decorator and uncomment the following line
# babel = Babel(app, locale_selector=get_locale)


@app.route('/', strict_slashes=False)
def index():
    """
    Route for the homepage

    This route is configured to the '/' URL.
    It returns the rendered '3-index.html' template.
    """
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run()
