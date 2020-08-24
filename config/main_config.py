from os import path
from os.path import dirname
from pathlib import Path
import pathlib
PROJECT_HOME = dirname(dirname(path.abspath(__file__)))
# needed path module as fileconfig file use unix parsing for writing log file
LOGGING_PATH = pathlib.PurePosixPath(Path(path.join(PROJECT_HOME,"logs","run_log.log")))