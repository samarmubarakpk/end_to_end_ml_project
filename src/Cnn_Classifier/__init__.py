# __init__.py inside the Cnn_Classifier directory

import os
import logging

# Define the logging configuration
logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
logdir = "logs"
logfile_path = os.path.join(logdir, "running_logs.log")

# Make sure the directory exists
os.makedirs(logdir, exist_ok=True)

# Set up the basic configuration for logging
logging.basicConfig(level=logging.INFO, format=logging_str, handlers=[
    logging.FileHandler(logfile_path),
    logging.StreamHandler()
])

# Create a logger instance
logger = logging.getLogger("cnnclassifierlogger")
