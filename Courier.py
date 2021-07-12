# -*- coding: UTF-8 -*-
from RepeatedTimer import RepeatedTimer
from datetime import datetime,timedelta
import queue,sys,random

class Order(object):
    orders=[]
    @classmethod
    def OrdercanEate(cls,obj):
        obj.q.put(obj)
        obj.trigger.stop()
        print('----> canEate: ', id(obj))
        obj.SetcanEate();

    def __init__(self, courier):
        self.canEate=0
        self.canEateTime=0
        self.HowlongToPrepare=4
        self.courier=courier
        self.courier.order = self
        self.waitTime=timedelta()
        self.pickupTime=0
        self.picked=0
        Order.orders.append(self)
        self.Event="OrdercanEate"
        self.trigger=RepeatedTimer(self.HowlongToPrepare,Order.OrdercanEate,self)
        self.q=courier.q

    def setWaitTime(self,now):
        assert self.courier.Arrived == 1
        self.waitTime = now - self.canEateTime
        self.getUpdateTime = now
        print('%s get updated %s' % (self.__class__, str(now)))

    def SetcanEate(self):
        now = datetime.now()
        self.canEate = 1
        self.canEateTime = now;
        if self.courier.Arrived == 1:
            self.courier.setWaitTime(now)
        else:
            assert self.courier.Arrived == 0



class Orders(object):
    def __init__(self, arg=None):
        self.arg = arg

    def GetNext():
        courier = Courier();
        o=Order(courier);
        courier.Order = o
        return o


class Courier(object):
    couriers=[]
    @classmethod
    def CourierArrived(cls,obj):
        obj.q.put(obj)
        print('------------> Arrived: ',id(obj))
        obj.trigger.stop()
        obj.SetArrived();

    def __init__(self, q):
        self.Arrived=0
        self.ArrivedTime=0
        self.HowlongToArrive=random.uniform(3,5)
        self.order=None
        self.waitTime=timedelta()
        Courier.couriers.append(self)
        self.seqNumber= len(Courier.couriers)
        self.Event='CourierArrived'
        self.trigger=RepeatedTimer(self.HowlongToArrive,Courier.CourierArrived,self)
        self.q=q

    

    def setWaitTime(self,now):
        assert self.order.canEate == 1
        self.waitTime = now - self.ArrivedTime
        self.getUpdateTime = now
        print('%s get updated %s' % (self.__class__,str(now)))

    def SetArrived(self):
        now = datetime.now()
        self.Arrived = 1
        self.ArrivedTime =now;
        self.order = Order.orders[self.seqNumber - 1]
        if self.order.canEate == 1:
            self.order.setWaitTime(now)
        else:
            assert self.order.canEate == 0

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    pass        

        
