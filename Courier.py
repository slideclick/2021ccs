# -*- coding: UTF-8 -*-
from RepeatedTimer import RepeatedTimer
import queue,sys
class Courier(object):
    """docstring for Courier"""

    couriers=[]
    @classmethod
    def CourierArrived(cls,obj):
        obj.q.put(obj)
        print('------------>',id(obj))
        obj.trigger.stop()

    def __init__(self, q):
        self.Arrived=0
        self.ArrivedTime=0
        self.HowlongToArrive=4
        # self.Order=order
        self.waitTime=0
        Courier.couriers.append(self)
        self.Event='CourierArrived'
        self.trigger=RepeatedTimer(self.HowlongToArrive,Courier.CourierArrived,self)
        self.q=q

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    q = queue.Queue()
    q.put(Courier(q))
    print(q.get())
    pass        

        
