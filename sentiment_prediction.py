from pathlib import Path
import logging
import logging.config
from config.main_config import PROJECT_HOME, LOGGING_PATH, LOGGING_CONFIG
import flask

logging.config.fileConfig(LOGGING_CONFIG,
                          disable_existing_loggers=False,
                          defaults={'log_dir': LOGGING_PATH})

logger = logging.getLogger("flask-app")

