# -*- coding: UTF-8 -*-
class Order(object):
    """docstring for Order"""

    orders=[]

    def __init__(self, courier=None):
        self.canEate=0
        self.canEateTime=0
        self.HowlongToPrepare=180
        self.Courier=courier
        self.waitTime=0
        self.pickupTime=0
        self.picked=0
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    pass        

        
