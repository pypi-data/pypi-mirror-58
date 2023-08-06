import logging
from dataclasses import dataclass
from typing import List
from openfizzbuzz.core.letter import Letter, LetterFactory

logger = logging.getLogger('word')


@dataclass
class Word:
    letters: List[Letter] = None

    def __repr__(self):
        return ''.join([letter.__repr__() for letter in self.letters])

    def __add__(self, other):
        return WordFactory.create_word(self.letters + other.letters)


class WordFactory:

    @staticmethod
    def create_word(chars):
        if not chars:
            raise ValueError('Attempted to create an empty word')

        if isinstance(chars[0], str):
            return Word(LetterFactory.create_letters(chars))
        elif isinstance(chars[0], Letter):
            return Word(chars)
