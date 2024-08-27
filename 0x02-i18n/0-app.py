#!/usr/bin/env python3
import flask


app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('0-index.html')

if __name__ == "__main__":
    app.run()