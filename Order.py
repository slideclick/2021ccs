# -*- coding: UTF-8 -*-
from Courier import Courier
from RepeatedTimer import RepeatedTimer
class Order(object):
    orders=[]
    @classmethod
    def OrdercanEate(cls,obj):
        obj.q.put(obj)
        print('---->',id(obj))
        obj.trigger.stop()

    def __init__(self, courier):
        self.canEate=0
        self.canEateTime=0
        self.HowlongToPrepare=4
        self.Courier=courier
        self.waitTime=0
        self.pickupTime=0
        self.picked=0
        Order.orders.append(self)
        self.Event="OrdercanEate"
        self.trigger=RepeatedTimer(self.HowlongToPrepare,Order.OrdercanEate,self)
        self.q=courier.q

class Orders(object):
    def __init__(self, arg=None):
        self.arg = arg

    def GetNext():
        courier = Courier();
        o=Order(courier);
        courier.Order = o
        return o
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    pass        

        
