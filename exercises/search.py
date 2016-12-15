"""Implementation av sökalgoritmer.

Fler alternativ finns beskrivna på Wikipedia_.

.. _Wikipedia: https://en.wikipedia.org/wiki/Binary_search_algorithm#Algorithm
"""


import logging


logger = logging.getLogger(__name__)


def binary_search(a, number):
    first_number = 0
    last_number = len(a) - 1

    while first_number <= last_number:
        logger.debug('Searching from {} to {}'.format(first_number, last_number))
        middlenumber = (first_number+last_number)//2
        logger.debug('Pivot element is at index {}'.format(middlenumber))
        if a[middlenumber] == number:
            return middlenumber
        else:
            if number <= a[middlenumber]:
                logger.debug('Moving upper limit to pivot.')
                last_number = middlenumber - 1
            if number >= a[middlenumber]:
                logger.debug('Moving lower limit to pivot.')
                first_number = middlenumber + 1
    return False
