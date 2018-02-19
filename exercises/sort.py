"""Implementation av sorteringsalgoritmer.

Fler alternativ finns beskrivna på Wikipedia_.

.. _Wikipedia: https://en.wikipedia.org/wiki/Sorting_algorithm#Popular_sorting_algorithms
"""


def bubble_sort(l):
    """Bubble sort.

    Implementation av bubble sort. En enkel algoritm men oftast mycket
    ineffektiv. Beskrivning finns på Wikipedia_.

    .. _Wikipedia: https://en.wikipedia.org/wiki/Sorting_algorithm#Popular_sorting_algorithms
    """
    run = len(l) - 1
    while run > 0:
        f = 0
        s = 1
        while run >= s:
            if l[f] > l[s]:
                temp = l[f]
                l[f] = l[s]
                l[s] = temp
                f += 1
                s += 1
            else:
                f += 1
                s += 1
        else:
            run += -1
    return l


def insertion_sort(l):
    """Insertion sort.

    Implementation av insertion sort. Beskrivning finns på Wikipedia_.

    .. _Wikipedia: https://en.wikipedia.org/wiki/Insertion_sort

    """
    i = 1
    while i < len(l):
        j = i
        while j > 0 and l[j-1] > l[j]:
            l[j], l[j - 1] = l[j - 1], l[j]
            j = j - 1
        i = i + 1
    return l


def selection_sort(l):
    """Selection sort.

    Implementation av selection sort. Beskrivning finns på Wikipedia_.

    .. _Wikipedia: https://en.wikipedia.org/wiki/Selection_sort

    i = 0
    j = 0
    n = 0
    for range(j n-1):
        j += 1
        iMin = j
        i = j + 1
        for i < n:
            i += 1
            if l[i] < l[iMin]:
                iMin = i;
                if iMin != j:
                    l[j], l[iMin] = l[iMin], l[j]
                    return l
        if l[i] > l[j]:
            mi = l[j]
            j += 1
        else:
            mi = l[i]
            if l[mi] > l[mi]:
    """
    i = 0
    while i < len(l):
        smallest = min(l[i:])
        ismall = l.index(smallest)
        l[i], l[ismall] = l[ismall], l[i]
        i=i+1
    else:
        return l
def merge_sort(l):
    """Merge sort.

    Implementation av merge sort. En av de mer effektiva sorteringsalgoritmerna.
    Beskrivning finns på Wikipedia_.

    .. _Wikipedia: https://en.wikipedia.org/wiki/Sorting_algorithm#Popular_sorting_algorithms

    """
    return l
