import pytest
from exercises.sort import merge_sort
from exercises.sort import insertion_sort
from exercises.sort import binary_search

def test_binary_search():
    """ tester av binary search """
    assert binary_search([1, 2, 3, 4, 5, 7, 9, 10], 3) == 2
    assert binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 5) == 4
    assert binary_search([2, 5, 6, 8, 10, 13], 13) == 5
    assert binary_search([4, 6, 7, 10, 11, 12], 4) == 0
    assert binary_search([-21, -15, -3, 1, 3, 5], -15) == 1
    assert binary_search([0, 1, 2], 0) == 0
    assert binary_search([], 5) == -1
    assert binary_search([1, 2, 3, 3, 4], 3) == 2

def test_insertion_sort():
    """ tester av sorteringsalgoritmer """
    assert insertion_sort([3, 4, 1, 2, 5]) == [1, 2, 3, 4, 5]
    assert insertion_sort([]) == []
    assert insertion_sort([3, 7, 10, 2, 7, 11, 1]) == [1, 2, 3, 7, 7, 10, 11]
    assert insertion_sort([100, 194, 678, 300200, 1337, 420]) == [100, 194, 420, 678, 1337, 300200]

def test_merge_sort():
    """ tester av sorteringsalgoritmer """
    assert merge_sort([5, 7, 4, 8, 1, 2, 6, 3, 9]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert merge_sort([]) == []
    assert merge_sort([2, 8, 5, 1, 13, 12, 3, 5]) == [1, 2, 3, 5, 5, 8, 12, 13]
    assert merge_sort([35, 4000000, 374, 364, 399276, 10043]) == [35, 364, 374, 10043, 399276, 4000000]
