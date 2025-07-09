import logging
import os

from from_root import from_root # this line assumes you have a package named `from_root` that provides the `from_root` function
from datetime import datetime # this line assumes you have a package named `datetime` that provides the `datetime` class

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log" # this line creates a log file name based on the current date and time
log_dir = 'logs' # this line specifies the directory where log files will be stored

logs_path = os.path.join(from_root(), log_dir, LOG_FILE) # this line constructs the full path to the log file by joining the root directory, log directory, and log file name
os.makedirs(log_dir, exist_ok=True) # this line creates the log directory if it does not exist

logging.basicConfig(    # this line configures the logging module
    filename=logs_path, # this line sets the file where logs will be written
    level=logging.DEBUG, # this line sets the logging level to DEBUG, meaning all messages at this level and above will be logged
    format= "[%(asctime)s] %(name)s - %(levelname)s - %(message)s", # this line specifies the format of the log messages, including the timestamp, log level, and message
)

# To create logging messages, you can use the following link:
# https://docs.python.org/3/library/logging.html