from dataclasses import dataclass
from typing import List
import logging

logger = logging.getLogger('letter')


@dataclass
class Letter:
    """
    Class representing a letter.
    The "dataclass" decorator creates an init(self, value) for us.
    """
    value: str = ''

    def __repr__(self):
        return self.value


class LetterFactory:
    """
    Factory in charge of creating Letter instances.
    """

    @staticmethod
    def create_letter(char) -> Letter:
        logger.debug(f'Creating letter {char} from factory')
        return Letter(char)

    @staticmethod
    def create_letters(chars: List[str]):
        logger.debug(f'Creating letters {chars} from factory')
        return [LetterFactory.create_letter(char) for char in chars]
