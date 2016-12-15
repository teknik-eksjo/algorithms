"""Implementation av sorteringsalgoritmer.

Fler alternativ finns beskrivna på Wikipedia_.

.. _Wikipedia: https://en.wikipedia.org/wiki/Sorting_algorithm#Popular_sorting_algorithms
"""

import logging
logger = logging.getLogger(__name__)


def binary_search(l1, value):
    """ Binary search for lists.

    WARNING: Doesn't necessarily work as expected with duplicates.
    """
    """vi ger min_ och max_ värdet av numrerna först och sist i listan"""
    min_ = 0
    max_ = len(l1) - 1
    logger.debug('New test')
    while True:
        logger.debug('Searching between {} and {}.'.format(min_, max_))
        if max_ < min_:
            """kollar om listan är tom"""
            logger.debug('ooops, your list apaers to be empty NOOOOB')
            return -1
        index = (min_ + max_) // 2
        if l1[index] < value:
            """sökta nummret finns vänster om mittersta numret"""
            min_ = index + 1
        elif l1[index] > value:
            """sökta nummret finns höger om mittersta numret"""
            max_ = index - 1
        else:
            """sökta numret är det mittersa numret"""
            logger.debug('index of wanted value is {}'.format(index))
            return index


def insertion_sort(l1):
    """
    jämför de två första talen, är det andra minder byter talen plats,
    annars fortsätter man och jämföra de andra talet och nästa tatl i listan,
    repetera tills listan är soterad
    """
    logger.debug('New test')
    for first in range(1, len(l1)):
        smallest = first
        logger.debug('comparing values on index {} and {}'.format(smallest-1, smallest))
        while smallest > 0 and l1[smallest] < l1[smallest-1]:
            l1[smallest], l1[smallest-1] = l1[smallest-1], l1[smallest]
            smallest = smallest-1
            logger.debug('smallerr value found!!')
            logger.debug('value on index {} and {} switch places'.format(smallest, smallest+1))
    return l1


def merge_sort(l1):
    """bryter upp listans tal och sätter sedan ihop listan sorterad"""
    logger.debug('sorting list {}'.format(l1))
    if len(l1) <= 1:
        return l1

    else:
        """delar upp listan i halvor tills talen är ensamma"""
        mid = len(l1)//2
        left = merge_sort(l1[:mid])
        right = merge_sort(l1[mid:])
        """
        sätt ihop ensamma talen till större och störrre soterade listor fram
        tills då en sorterad l1 ha skapats
        """
        left_counter, right_counter, master_counter = 0, 0, 0

        while left_counter < len(left) and right_counter < len(right):
            if left[left_counter] < right[right_counter]:
                l1[master_counter] = left[left_counter]
                left_counter += 1
                master_counter += 1
            else:
                l1[master_counter] = right[right_counter]
                right_counter += 1
                master_counter += 1

        while left_counter < len(left):
            l1[master_counter] = left[left_counter]
            left_counter += 1
            master_counter += 1

        while right_counter < len(right):
            l1[master_counter] = right[right_counter]
            right_counter += 1
            master_counter += 1
        logger.debug('return {}'.format(l1))

        return l1
