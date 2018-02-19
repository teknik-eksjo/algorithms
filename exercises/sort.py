"""Implementation av sorteringsalgoritmer.

Fler alternativ finns beskrivna på Wikipedia_.

.. _Wikipedia: https://en.wikipedia.org/wiki/Sorting_algorithm#Popular_sorting_algorithms
"""
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


def bubble_sort(l):
    """Bubble sort.

    Implementation av bubble sort. En enkel algoritm men oftast mycket
    ineffektiv. Beskrivning finns på Wikipedia_.

    .. _Wikipedia: https://en.wikipedia.org/wiki/Sorting_algorithm#Popular_sorting_algorithms
    """
    # x=True
    # while x==True:
    #     for i in range(len(l)-1, 0 ,-1):
    #         x=False
    #         if l[i]> l[i+1]:
    #             l[i], l[i+1] = l[i+1], l[i]  # Swap
    #             x=True
    #
    # return l


    for i in range(len(l)-1, 0, -1):
        for j in range(i):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]  # Byt plats
    return l

def insertion_sort(l):
    """Insertion sort.

    Implementation av insertion sort. Beskrivning finns på Wikipedia_.

    .. _Wikipedia: https://en.wikipedia.org/wiki/Insertion_sort

    """
    # x= True
    # for i in range(0, len(l)-1):
    #     while x == True:
    #         if l[i]> l[i+1]:
    #             l[i], l[i+1] = l[i+1], l[i]
    #             i -=1
    #             if i==1:
    #                 x=False
    # return l

    logger.debug('Starting sort of list \n{}'.format(l))
    for i in range(1, len(l)):
        logger.debug('Iteration starts with list \n{}'.format(l))
        j = i
        logger.debug('Comparing {} (i) and {} (j).'.format(i, j))
        while j > 0 and l[j-1] > l[i]:
            j -= 1
        logger.debug('Swapping index {} (i) and {} (j).'.format(i, j))
        l = l[:j] + [l[i]] + l[j:i] + l[i+1:]

    return l


def selection_sort(l):
    """Selection sort.

    Implementation av selection sort. Beskrivning finns på Wikipedia_.

.. _Wikipedia: https://en.wikipedia.org/wiki/Selection_sort

    """
#    for i in range(1, len(l), -1):
#        for j in range(i):
#            k = j[l]


    for i in range(len(l)):
        minst = i
        for n in range(i+1, len(l)):
            if l[minst] > l[n]:
                minst = n
        l[i], l[minst] = l[minst], l[i]
    return l


def merge_sort(l):
    """Merge sort.

    Implementation av merge sort. En av de mer effektiva sorteringsalgoritmerna.
    Beskrivning finns på Wikipedia_.

    .. _Wikipedia: https://en.wikipedia.org/wiki/Sorting_algorithm#Popular_sorting_algorithms

    """
    length = len(l)
    if length == 1:
        return l

    pivot = int(length/2)
    left = merge_sort(l[:pivot])
    right = merge_sort(l[pivot:])

    result = []
    while True:
        if len(left) == 0:
            result.extend(right)
            return result

        if len(right) == 0:
            result.extend(left)
            return result

        if left[0] > right[0]:
            result.append(right.pop(0))
        else:
            result.append(left.pop(0))


    # for n in range(len(l)):
    #     halva = len(l)/2
    #     Första_halvan = [:halva]
    #     Andra_halvan = [halva:]
    #
    #
    #     if l[0]
    #
    # return l
