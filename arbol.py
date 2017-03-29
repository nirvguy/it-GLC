import re

def add_tabs(s):
    return s.replace('\n', '\n\t')

class BinaryTree:
    def __init__(self, v, l = None, r = None):
        self.v = v
        self.l = l
        self.r = r

    def __str__(self):
        output = str(self.v)
        if self.l is not None:
            output += "\n\tl." + add_tabs(str(self.l))
        if self.r is not None:
            output += "\n\tr." + add_tabs(str(self.r))
        return output

def all_naturals(n):
    i = 0
    while True:
        yield i
        i = i+1

def all_pairs_with_sum(n):
    return ((i, n-i) for i in range(0,n+1))

def all_bintrees(n):
    if n == 0:
        yield None
    else:
        for i,j in all_pairs_with_sum(n-1):
            for l in all_bintrees(i):
                for r in all_bintrees(j):
                    yield BinaryTree("a", l, r)
