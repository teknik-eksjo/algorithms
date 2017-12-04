import pytest
from exercises.search import linear_search, binary_search



def test_linear_search():
    assert linear_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 4) == 3
    assert linear_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 1) == 0
    assert linear_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 9) == 8
    assert linear_search([-4, -2, 1, 3, 9, 14, 17, 23], -2) == 1
    assert linear_search([1.2, 3.6, 9, 14.22, 17, 23], 14.22) == 3
    assert linear_search([7], 7) == 0

    with pytest.raises(ValueError):
        linear_search([1, 2, 3, 6, 7], 4)

    with pytest.raises(ValueError):
        linear_search([], 7)


@pytest.mark.skip('Not implemented yet.')
def test_binary_search():
    assert binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 4) == 3
    assert binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 1) == 0
    assert binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 9) == 8

    assert binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 5) == 4
    assert binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) == 4
    assert binary_search([1, 2, 3, 4, 5, 6, 7, 8], 5) == 4

    assert binary_search([-4, -2, 1, 3, 9, 14, 17, 23], -2) == 1
    assert binary_search([1.2, 3.6, 9, 14.22, 17, 23], 14.22) == 3
    assert binary_search([7], 7) == 0

    with pytest.raises(ValueError):
        binary_search([1, 2, 3, 6, 7], 4)

    with pytest.raises(ValueError):
        binary_search([], 7)
