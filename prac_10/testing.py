"""
CP1404/CP5632 Practical 10
Testing demo using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python")
    True
    """
    return len(word) > length


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"

    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    test_car = Car()
    assert test_car._odometer == 0, "Car does not set odometer correctly"

    test_car = Car(fuel=10)
    assert test_car.fuel == 10, "Car does not set fuel correctly"
    test_car.add_fuel(20)
    assert test_car.fuel == 30, "Car does not set value passed in fuel correctly"


run_tests()

doctest.testmod()


def format_phrase(phrase):
    """
    Format phrase into a sentence
    >>> format_phrase('hello')
    'Hello.'
    >>> format_phrase('It is an ex parrot.')
    'It is an ex parrot.'
    >>> format_phrase('I like apple')
    'I like apple.'
    """
    words = phrase.split()
    words[0] = words[0].title()
    sentence = " ".join(words)
    if sentence[-1] != '.':
        sentence += '.'
    return sentence