# -*- coding: UTF-8 -*-
from RepeatedTimer import RepeatedTimer
from datetime import datetime


import queue,sys
class Courier(object):
    """docstring for Courier"""

    couriers=[]
    @classmethod
    def CourierArrived(cls,obj):
        obj.q.put(obj)
        print('------------>',id(obj))
        obj.trigger.stop()
        obj.SetArrived();

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

    def SetArrived(self):
        self.Arrived = 1
        self.ArrivedTime = datetime.now();
        if self.Order.canEate == 1:
            self.waitTime = 0
        else:
            pass    

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    q = queue.Queue()
    q.put(Courier(q))
    print(q.get())
    pass        

        
