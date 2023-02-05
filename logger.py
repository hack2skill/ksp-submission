import logging
from logging.handlers import RotatingFileHandler

# Main logger
log = logging.getLogger()
log.setLevel(logging.DEBUG)

# Debug Logger
formatter = logging.Formatter("%(asctime)s : %(levelname)s : [%(filename)s:%(lineno)s - %(funcName)s()] : %(message)s")
debug_handler = RotatingFileHandler("logs/debug",maxBytes=5000000,backupCount=5)
debug_handler.setLevel(logging.DEBUG)
debug_handler.setFormatter(formatter)
log.addHandler(debug_handler)


# Error Logger
formatter = logging.Formatter("%(asctime)s : [%(filename)s: %(funcName)s()] : %(message)s")
error_handler = logging.FileHandler("logs/error")
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(formatter)
log.addHandler(error_handler)

# Info Logger
formatter = logging.Formatter("%(asctime)s : %(message)s")
info_handler = logging.FileHandler("logs/info")
info_handler.setLevel(logging.INFO)
info_handler.setFormatter(formatter)
log.addHandler(info_handler)