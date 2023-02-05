"""
Purpose: Read the configurations from YAML file
"""

import yaml
from Scripts.Utility import utils

def read_configuration(file_name):
    with open(file_name, "r") as fl:
        try:
            return yaml.load(stream=fl, Loader=yaml.FullLoader)
        except yaml.YAMLError as exc:
            utils.logger.error("Configuration File Read Error" + str(file_name) + "ERROR" + str(exc))