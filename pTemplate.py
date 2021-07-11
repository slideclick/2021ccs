# -*- coding: UTF-8 -*-

class A(object):
    """ A class
    >>> a=A(2);print(a.v)
    3
    """
    def __init__(self, v):
        self.v = 3# v will fail the doctest

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    pass
