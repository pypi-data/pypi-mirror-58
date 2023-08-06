import logging
from logging.handlers import RotatingFileHandler
from logging import config as logging_conf

from openfizzbuzz.config import logging_config

# Logging configuration loading
logging_conf.dictConfig(logging_config.LOGCONFIG)
logger = logging.getLogger('settings')


logger.debug('Loading configuration')


# Use a predefined logging configuration
LOGCONFIG = logging_config.LOGCONFIG
