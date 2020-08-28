from flask import Flask
import logging
import logging.config
from config.main_config import LOGGING_PATH, LOGGING_CONFIG

'''This is the flask app and builds the webpage interface for the model.'''

app = Flask(__name__)
app.config.from_object('config.flask_config')

logging.config.fileConfig(LOGGING_CONFIG,
                          disable_existing_loggers=False,
                          defaults={'log_dir': LOGGING_PATH})
logger = logging.getLogger("app")

@app.route("/")
@app.route("/home")
def home():
    return "<h1>Home Page!<h1>"

@app.route("/about")
def about():
    return "<h1>About Page!<h1>"