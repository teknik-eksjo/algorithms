"""Övningar på sökalgoritmer."""


def linear_search(l, v):
    """Implementation av sequential search.

    Detta är den naiva algoritmen för sökning i listor (eller arrayer), se
    Wikipedia_. Fördelen är att den fungerar även för osorterade listor.

    Funktionen ska returnera indexet för det sökta värdet `v` i listan `l`. Om
    inte det sökta värdet, `v`, finns i listan `l` ska istället undantaget
    `ValueError` kastas.

    .. _Wikipedia: https://en.wikipedia.org/wiki/Linear_search#Basic_algorithm
    """
    found = False
    for i in range(len(l)):
        if(l[i] == v):
            found = True
            return i

    if(found == False):
        raise ValueError

def binary_search(l, v):
    """Implementation av binary search.

    Detta är den klassiska algoritmen för sökning i sorterade listor (eller
    arrayer), se Wikipedia_.

    Funktionen ska returnera indexet för det sökta värdet `v` i listan `l`. Om
    inte det sökta värdet, `v`, finns i listan `l` ska istället undantaget
    `ValueError` kastas.

    .. _Wikipedia: https://en.wikipedia.org/wiki/Binary_search_algorithm#Algorith
    c = (len(l) - 1) // 2

    while c < len(l):
        if l[c] == v:
            return c
        else:
            if l[c] > v:
                c = len(l) // c
            else:
                c = c
    """
    first = 0
    last = len(l) - 1

    while first <= last:
        i = (first + last) // 2

        if l[i] == v:
            return i
        elif l[i] > v:
            last = i - 1
        elif l[i] < v:
            first = i + 1
    else:
        raise ValueError
