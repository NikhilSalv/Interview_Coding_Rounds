import pytest
from exercise1 import is_palindrome

def test_palindrome_with_alphanumeric():
    assert is_palindrome("A man, a plan, a canal, Panama") is True
    assert is_palindrome("No lemon, no melon") is True

def test_palindrome_with_numbers():
    assert is_palindrome("12321") is True
    assert is_palindrome("1221") is True
    assert is_palindrome("12345") is False

def test_non_palindrome():
    assert is_palindrome("hello") is False
    assert is_palindrome("world") is False

def test_empty_string():
    assert is_palindrome("") is True

def test_single_character():
    assert is_palindrome("a") is True
    assert is_palindrome("Z") is True

def test_mixed_case():
    assert is_palindrome("RaceCar") is True
    assert is_palindrome("MadAm") is True