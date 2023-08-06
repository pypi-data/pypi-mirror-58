"""
FizzBuzz printing function
"""
import logging

from openfizzbuzz.core.word import WordFactory

logger = logging.getLogger('fizzbuzz')


def fizzbuzz(start: int, stop: int) -> None:
    """
    Actual fizzbuzz function
    :param start: int: Number to start fizzbuzzing
    :param stop: int: Number to stop fizzbuzzing
    :return: None
    """
    logger.debug(f'FizzBuzzing from {start} to {stop+1}')
    fizz = WordFactory.create_word('Fizz')
    buzz = WordFactory.create_word('Buzz')
    _fizzbuzz = fizz + buzz

    for i in range(start, stop+1):
        if not i % 3 and not i % 5:
            print(_fizzbuzz)
        elif not i % 3:
            print(fizz)
        elif not i % 5:
            print(buzz)
        else:
            print(i)
