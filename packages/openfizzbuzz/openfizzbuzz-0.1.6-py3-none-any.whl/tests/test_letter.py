import pytest
from openfizzbuzz.core.letter import Letter, LetterFactory


def test_letter_instantiation():
    a = Letter('A')
    assert a is not None
    assert isinstance(a, Letter)


def test_letter_value():
    a = Letter('A')
    b = Letter('1')
    assert a.value == 'A'
    assert isinstance(b.value, str)
    assert b.value == '1'


def test_letter_factory_create_letter():
    a = LetterFactory.create_letter('A')
    assert a is not None
    assert isinstance(a, Letter)
    assert a.value == 'A'


def test_letter_factory_create_letters():
    letters = ['A', 'B', '1']
    a, b, one = LetterFactory.create_letters(letters)
    assert all((a, b, one))
    assert isinstance(a, Letter)
    assert a.value == 'A'
    assert b.value == 'B'
    assert one.value == '1'
