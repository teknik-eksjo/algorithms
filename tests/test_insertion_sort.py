import pytest
from exercises.sort import merge_sort
from exercises.sort import insertion_sort
from exercises.sort import binary_search

def test_binary_seatch():
    """test av sorterongsalgoritmer"""
    assert binary_search([0, 3, 6, 9, 10, 21], 9) == 3
    assert binary_search([9, 21, 41, 73, 99, 101], 101) == 5
    assert binary_search([-3, -1, 0, 1, 4], -1) == 1
    assert binary_search([1234, 2345, 3456, 4567, 5678, 6789], 1234) == 0
    assert binary_search([], 3) == -1

def test_insertion_sort():
    """test av sorterongsalgoritmer"""
    assert insertion_sort([5, 7, 4, 8, 1, 2, 6, 3]) == [1, 2, 3, 4, 5, 6, 7, 8]
    assert insertion_sort([]) == []
    assert insertion_sort([9, 7, 3, 120, 674, 1, 6, 9]) == [1, 3, 6, 7, 9, 9, 120, 674]
    assert insertion_sort([69, 911, 666, 5500, 420, 1337]) == [69, 420, 666, 911, 1337, 5500]

def test_merge_sort():
    """test av sorterongsalgoritmer"""
    assert merge_sort([5, 7, 4, 8, 1,  2, 6, 3]) == [1, 2, 3, 4, 5, 6, 7, 8]
    assert merge_sort([]) == []
    assert merge_sort([9, 5, 3, 12, 24, 1, 6, 9]) == [1, 3, 5, 6, 9, 9, 12, 24]
    assert merge_sort([2421, 1279, 17, 5362, 3526, 12345]) == [17, 1279, 2421, 3526, 5362, 12345]
