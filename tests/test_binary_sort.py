import pytest
from exercises.search import binary_sort

def test_binary_sort():
    l = [2, 4, 7, 10, 27, 34, 35]
    assert binary_sort(l, 34)
