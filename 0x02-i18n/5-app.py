#!/usr/bin/env python3
"""
File: 3-app.py

A simple flask app with babel extension

Author: Malik Hussein
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

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
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
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
    return render_template('5-index.html')

def get_user():
    user_id = request.args.get('login_as')
    if user_id is None:
        return None
    return users.get(int(user_id))

@app.before_request
def before_request():
    user = get_user()
    g.user = user

if __name__ == "__main__":
    app.run()
