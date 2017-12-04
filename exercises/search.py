"""Övningar på sökalgoritmer.
"""


def linear_search(l, v):
    """Implementation av sequential search.

    Detta är den naiva algoritmen för sökning i listor (eller arrayer), se
    Wikipedia_. Fördelen är att den fungerar även för osorterade listor.

    Funktionen ska returnera indexet för det sökta värdet `v` i listan `l`. Om
    inte det sökta värdet, `v`, finns i listan `l` ska istället undantaget
    `ValueError` kastas.

    .. _Wikipedia: https://en.wikipedia.org/wiki/Linear_search#Basic_algorithm
    """

    for i in range(0, len(l)):
        if l[i] == v:
            return i
    raise ValueError


def binary_search(l, v):
    """Implementation av binary search.

    Detta är den klassiska algoritmen för sökning i sorterade listor (eller
    arrayer), se Wikipedia_.

    Funktionen ska returnera indexet för det sökta värdet `v` i listan `l`. Om
    inte det sökta värdet, `v`, finns i listan `l` ska istället undantaget
    `ValueError` kastas.

    .. _Wikipedia: https://en.wikipedia.org/wiki/Binary_search_algorithm#Algorith
    """
    
