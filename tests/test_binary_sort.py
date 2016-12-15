import pytest
from exercises.search import binary_search

def test_binary_sort():
    a = [1, 1, 3, 6, 8, 13, 431]
    assert binary_search(a, 8) == 4
    assert binary_search(a, 3) == 2
    assert binary_search(a, 1) == 1
    assert binary_search(a, 1) == 0
    assert binary_search(a, 55) == False

def test_binary_sort():
    a = [1, 1, 2, 3, 555, 7123, 10000, 777777]
    assert binary_search(a, 777777) == 7
    assert binary_search(a, 12321312) == False
