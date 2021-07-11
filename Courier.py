# -*- coding: UTF-8 -*-
class Courier(object):
    """docstring for Courier"""

    courier=[]

    def __init__(self, order=None):
        self.Arrived=0
        self.ArrivedTime=0
        self.HowlongToArrive=13
        self.Order=order
        self.waitTime=0
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    pass        

        
