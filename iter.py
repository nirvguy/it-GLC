#!/usr/bin/python3
from itertools import count, tee

def int_lists_with_sum(n, dim=2):
    if dim == 0:
        yield []
    elif dim == 1:
        yield [n]
    else:
        # All lists that sum @n of lenght @dim are of the form
        # [i, a_1, ..., a_n-1] where [a_1,...,a_n-1] is a list of length @n-1
        # that sums n-i
        for i in range(0, n+1):
            j = n-i
            for j in int_lists_with_sum(j, dim-1):
                yield [i] + j

def all_lists(dim=None):
    """ Returns an iterator of all the posibles list of naturals of length @dim.

        If @dim is not specified then returns all list for every possible length
    """
    if dim is not None:
        # Iter all posible list of length @dim by going to all the list with
        # sum k for every k=1..
        for n in count():
            for l in all_lists_with_sum(n, dim):
                yield l
    else:
        # Iter all posible lists, going from list with lenght 1 to infinity
        for length in count():
            for l in all_lists(length):
                yield l

def position(iterable, n):
    """ Take the n-th element of the iterable """
    _, it = tee(iterable)
    for i, e in enumerate(it):
        if i == n:
            return e
            break

def product(*iterables):
    """Returns an iterator to the cartesian product of all the iterables passed
    as arguments. 

    The difference with itertools.product is that this 
    still works even if those iterators are infinite.

    Example:
        >> a = count() # 1, 2, 3, ..
        >> b = (lambda x: x**2 for x in count()) # 1, 4, 9, ...
        >> list(take(product(a, b), 6)) == [(1,1), (2, 1), (1, 4), (3, 1), (2, 4), (1,9)]
    """
    iterators = list(map(iter, iterables))
    dim = len(iterators)
    for cords in all_lists(dim):
        elements = []
        n = 0
        for j, it in enumerate(j, iterators):
            try:
                yield position(it, cords[j])
            except StopIteration:
                n += 1
                continue
        if n == dim:
            break


def take(iterable, n):
    """Returns an iterator to the first n elements from iterable"""
    for i, e in enumerate(iterable):
        if i >= n:
            break
        yield e

def union(*iterables):
    """Returns an iterator to the elements from the union of all the iterators
       passed as argument even if each one is infinite.

    Example:
        >> a = (2**x for x in count()) # 1, 2, 4, 8, 16
        >> b = (3**x for x in count()) # 1, 3, 9, 27, 81
        >> list(take(union(a,b), 10)) = [1, 1, 2, 3, 4, 9, 8, 27, 16, 81]
       """
    iterators = list(map(iter, iterables))
    n = 0
    while n < len(iterables):
        n = 0
        for it in iterators:
            try:
                yield next(it)
            except StopIteration:
                n += 1
