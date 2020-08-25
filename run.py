''' This is a central location to run all files'''
from app import app
from config.main_config import LOGGING_PATH, LOGGING_CONFIG
import logging.config

logging.config.fileConfig(LOGGING_CONFIG,
                          disable_existing_loggers=False,
                          defaults={'log_dir': LOGGING_PATH})
logger = logging.getLogger("run_sentiment_prediction")


def run_app():
    app.run(debug=app.config['DEBUG'])

if __name__=='__main__':
    run_app()

