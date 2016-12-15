"""Implementation av sökalgoritmer.

Fler alternativ finns beskrivna på Wikipedia_.

.. _Wikipedia: https://en.wikipedia.org/wiki/Binary_search_algorithm#Algorithm
"""


def binary_sort(l, number):
    first = 0
    last = len(l) - 1
    found = False

    while first <= last:
        middlenumber = (first + last)//2
        if l[middlenumber] == number:
            return middlenumber
        else:
            if number <= l[middlenumber]:
                last = middlenumber - 1
            if number >= l[middlenumber]:
                first = middlenumber + 1
    return found
