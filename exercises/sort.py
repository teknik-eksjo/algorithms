"""Implementation av sorteringsalgoritmer.

Fler alternativ finns beskrivna på Wikipedia_.

.. _Wikipedia: https://en.wikipedia.org/wiki/Sorting_algorithm#Popular_sorting_algorithms
"""


def insertion_sort(l):
            for n in range(1, len(l)):
                d = n
                while d > 0 and l[d] < l[d-1]:
                    l[d], l[d-1] = l[d-1], l[d]
                    d = d-1
                return l
