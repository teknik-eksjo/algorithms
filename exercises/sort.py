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
    for passnum in range(len(l)-1,0,-1):
        for i in range(passnum):
            if l[i]>l[i+1]:
                temp = l[i]
                l[i] = l[i+1]
                l[i+1] = temp
    return l



def insertion_sort(l):
    """Insertion sort.

    Implementation av insertion sort. Beskrivning finns på Wikipedia_.

    .. _Wikipedia: https://en.wikipedia.org/wiki/Insertion_sort

    """
    for index in range(1,len(l)):

     currentvalue = l[index]
     position = index

     while position>0 and l[position-1]>currentvalue:
         l[position]=l[position-1]
         position = position-1

     l[position]=currentvalue

    return l


def selection_sort(l):
    """Selection sort.

    Implementation av selection sort. Beskrivning finns på Wikipedia_.

    .. _Wikipedia: https://en.wikipedia.org/wiki/Selection_sort

    """
    for fillslot in range(len(l)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if l[location]>l[positionOfMax]:
               positionOfMax = location

       temp = l[fillslot]
       l[fillslot] = l[positionOfMax]
       l[positionOfMax] = temp
    return l


def merge_sort(l):
    """Merge sort.

    Implementation av merge sort. En av de mer effektiva sorteringsalgoritmerna.
    Beskrivning finns på Wikipedia_.

    .. _Wikipedia: https://en.wikipedia.org/wiki/Sorting_algorithm#Popular_sorting_algorithms

    """
    if len(l)>1:
        mid = len(l)//2
        lefthalf = l[:mid]
        righthalf = l[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                l[k]=lefthalf[i]
                i=i+1
            else:
                l[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            l[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            l[k]=righthalf[j]
            j=j+1
            k=k+1
    return l
