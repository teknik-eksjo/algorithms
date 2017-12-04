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
    for i in range(0,len(l)):
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
    #if len(l)==0 or (len(l))==1 and (l[0]!=v):
    #    raise ValueError

    #mid=l[len(l)//2]

    #if v==mid: return v
    #if v<mid: return binary_search(l[:len(l)//2], v)
    #if v>mid: return binary_search(l[len(l)//2+1:], v)
    low = 0
    high = len(l)-1


    while low <= high:
        mid = (low + high) // 2
        if l[mid] == v:
            return mid
        elif v < l[mid]:
            high = mid - 1
        else:
            low = mid + 1
    raise ValueError
