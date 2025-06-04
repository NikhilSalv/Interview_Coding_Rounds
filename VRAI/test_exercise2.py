import pytest
from exercise2 import find_first_duplicate

def test_with_duplicates():
    assert find_first_duplicate([1, 2, 3, 4, 2, 5, 6]) == 2
    assert find_first_duplicate([3, 1, 3, 4, 5]) == 3
    assert find_first_duplicate([10, 20, 10, 30, 40]) == 10

def test_without_duplicates():
    assert find_first_duplicate([1, 2, 3, 4, 5]) == -1
    assert find_first_duplicate([]) == -1

def test_single_element():
    assert find_first_duplicate([1]) == -1

def test_multiple_duplicates():
    assert find_first_duplicate([1, 2, 3, 2, 3, 4]) == 2
    assert find_first_duplicate([5, 5, 5, 5]) == 5

def test_with_negative_numbers():
    assert find_first_duplicate([-1, -2, -3, -1, -4]) == -1
    assert find_first_duplicate([-1, -2, -3, -4]) == -1

def test_with_mixed_numbers():
    assert find_first_duplicate([1, -1, 2, -2, 1]) == 1
    assert find_first_duplicate([0, 1, 0, 2, 3]) == 0