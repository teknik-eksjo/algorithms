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
    plats= 0
    for nummer in l:
        if nummer == v:
            return plats
        else:
            plats +=1
    else:
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

"""    nedre_plats = 0
    övre_plats = len(l)-1
    for nummer in l:
        if (nedre_plats + övre_plats)/2==0:


        else:
            if l[övre_plats/2]>v:
                nedre_plats = övre_plats/2
            else:
                övre_plats = övre_plats/2

    return

        else:"""
