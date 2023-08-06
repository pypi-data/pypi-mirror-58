import logging
from openfizzbuzz.config import settings
from openfizzbuzz.core import fizzbuzz

logger = logging.getLogger('main')


def run():
    """
    Entry point function for the module.
    """
    logger.info('Starting program')
    fizzbuzz.fizzbuzz(1, 100)


if __name__ == '__main__':

    run()
