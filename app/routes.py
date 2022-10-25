from flask import render_template
from app import app

@app.route('/')
def index():
    return 'Hello'

@app.route('/fave5')
def fave5():
    shows = ['Mad Men', 'Curb Your Enthusiasm', 'The Witcher', 'What We Do in the Shadows', 'Psych']
    return render_template('index.html', shows = shows)
