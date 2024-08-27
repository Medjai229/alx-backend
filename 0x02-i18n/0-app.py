#!/usr/bin/env python3
"""
File: 0-app.py

A simple flask app with babel extension

Author: Malik Hussein
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """
    Route for the homepage

    This route is configured to the '/' URL.
    It returns the rendered '0-index.html' template.
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run()
