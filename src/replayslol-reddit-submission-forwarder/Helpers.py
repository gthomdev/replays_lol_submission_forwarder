import logging
import yaml


def load_config(file_path):
    try:
        configuration = yaml.safe_load(open(file_path))
    except FileNotFoundError:
        logging.error("Config file not found")
        raise
    return configuration
