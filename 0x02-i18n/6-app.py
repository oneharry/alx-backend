#!/usr/bin/env python3
"""Basic flas app"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)

class Config:
    """Config class"""
    LANGUAGES = ['en', 'fr']
    babel_default_locale = 'en'
    babel_default_timezone = 'UTC'

app.config.from_object(Config)

babel = Babel(app)

@babel.localeselector
def get_locale() -> str:
    """Local func """
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/', strict_slashes=False)
def index() -> str:
    """Render a html """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
