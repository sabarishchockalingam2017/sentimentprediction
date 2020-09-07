from flask import Flask, render_template, url_for
import logging
import logging.config
from config.main_config import LOGGING_PATH, LOGGING_CONFIG
import os

'''This is the flask app and builds the webpage interface for the model.'''

app = Flask(__name__)
app.config.from_object('config.flask_config')

logger = logging.getLogger("app")

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='Home')

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/dataset")
def dataset():
    return render_template('dataset.html', title='Dataset')

@app.route("/model")
def model():
    return render_template('model.html', title='Model')


@app.context_processor
def override_url_for():
    ''' New CSS is not udpated due to browser cache. This function appends time to css path to make the updated CSS seem
    like a new file. '''
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    ''' This function appends the date to the css path'''
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

