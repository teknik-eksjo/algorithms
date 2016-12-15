import pytest
from exercises.search import binary_sort

def test_binary_sort():
    l = [2, 4, 7, 10, 27, 34, 35]
    assert binary_sort(l, 34) == 5

def test_binary_sort():
    l = [2, 34, 76, 131, 213, 899]
    assert binary_sort(l, 213) == 4
    assert binary_sort(l, 2) == 0
    assert binary_sort(l, 899) == 5
    
