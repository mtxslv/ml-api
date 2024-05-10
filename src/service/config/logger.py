"""Define function for create logger."""

import logging

from src.service.config.settings import settings

## from google.cloud import logging as gcloud_logging

logging.basicConfig(
    level = logging.DEBUG,
    format = settings.LOG_FORMAT,
    handlers = [logging.StreamHandler()],
)

def get_logger(name: str = __name__):
    return logging.getLogger(name=name)