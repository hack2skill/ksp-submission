"""
Logger Utility
"""

import logging.handlers
import os
import time
import datetime

class Logger:
    """
    Contain method for logger class
    """
    def __init__(self, config):
        """

        :param config:
        """
        print("3. Log>>logger.py file")
        ts = time.time()

        service_name = config["service_name"]
        log_dir_path = config["path"]["log_path"]

        if not os.path.isdir(log_dir_path):
            os.makedirs(log_dir_path)

        log_file = os.path.join(log_dir_path, service_name)

        formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s", "%Y-%m-%d %H:%M%S")

        logHandler = logging.handlers.TimedRotatingFileHandler(filename=str(log_file), backupCount=2, when="M", interval=600)
        logHandler.setLevel(config["log_level"])
        logHandler.setFormatter(formatter)

        # Instantiating the "logging.getLogger()" class ...
        self.log_obj = logging.getLogger(service_name)
        self.log_obj.addHandler(logHandler)
        self.log_obj.setLevel(config["log_level"])
        self.log_obj.debug("Logger Initialized")