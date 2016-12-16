import pytest
from exercises.sort import insertion_sort


def test_insertion_sort():
    l = [5, 7, 4, 8, 1, 2, 6, 3]
    assert insertion_sort(l) == [1, 2, 3, 4, 5, 6, 7, 8]
def test_intertion_sort():
    l = [4, 5, 6, 2, 5, 6, 2, 5, 1, 5,]
    assert insertion_sort(l) == [1, 2, 2, 4, 5, 5, 5, 5, 6, 6]
