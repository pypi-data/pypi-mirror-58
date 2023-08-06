import pytest
from openfizzbuzz.core.letter import Letter, LetterFactory


def test_letter_instantiation():
    assert isinstance(Letter('A'), Letter)
