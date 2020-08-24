from pathlib import Path
import logging
import logging.config
from config.main_config import PROJECT_HOME, LOGGING_PATH

logging.config.fileConfig(Path(PROJECT_HOME, "config", "logging", "local.conf"),
                          disable_existing_loggers=False,
                          defaults={'log_dir': LOGGING_PATH})
logger = logging.getLogger(__name__)

logger.info("Is this working.")
