"""Implementation av sorteringsalgoritmer.

Fler alternativ finns beskrivna på Wikipedia_.

.. _Wikipedia: https://en.wikipedia.org/wiki/Sorting_algorithm#Popular_sorting_algorithms
"""


def insertion_sort(l):
            for n in range(1, len(l)):
                d = l[n]
                a = n - 1
                while a >= 0 and l[a] > d:
                    l[a + 1] = l[a]
                    a = a - 1
                l[a+1] = d
            return l
