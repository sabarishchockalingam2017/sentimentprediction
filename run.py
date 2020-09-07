from app.app import app
from config.main_config import LOGGING_PATH, LOGGING_CONFIG
import logging.config
from flask import request

''' This is a central location to run all files.'''

logging.config.fileConfig(LOGGING_CONFIG,
                          disable_existing_loggers=False,
                          defaults={'log_dir': LOGGING_PATH})
logger = logging.getLogger("run_sentiment_prediction")


def run_app():
    'Boots up app on server.'
    app.run(debug=app.config['DEBUG'], port=app.config['PORT'])

def shutdown_server():
    'Forces flask app server shutdown.'
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

if __name__=='__main__':
    run_app()

