from flask import Flask, render_template, url_for, flash
from app.forms import InputForm
import logging
import logging.config
from config.main_config import LOGGING_PATH, LOGGING_CONFIG
import os
import app.helpers.prediction_handler as predhand

'''This is the flask app and builds the webpage interface for the model.'''

app = Flask(__name__)
app.config.from_object('config.flask_config')

#need secret key to verify safe access and prevent security attacks
app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY')

logger = logging.getLogger("app")


@app.route("/", methods=['GET','POST'])
@app.route("/home", methods=['GET','POST'])
def home():
    form = InputForm()

    if form.validate_on_submit():
        logger.debug("Recieved input:{}".format(form.userinput.data))
        sentpred = predhand.get_prediction(form.userinput.data)
        flash(f'{sentpred}','success')
        logger.debug("Predicted {}".format(sentpred))

    return render_template('home.html',
                           title='Home',
                           form=form)

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

