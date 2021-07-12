# -*- coding: UTF-8 -*-
from RepeatedTimer import RepeatedTimer
from datetime import datetime,timedelta
import queue,sys,random
import threading

from Config import ConfigParser
global debugFlag 
global OrdersPerSecond
debugFlag = ConfigParser.config_dic['Debug']
OrdersPerSecond = ConfigParser.config_dic['OrdersPerSecond']

class Order(object):
    orders=[]
    @classmethod
    def OrdercanEate(cls,obj):
        obj.trigger.stop()
        print('----> canEate: ', id(obj)) if debugFlag == '1' else None
        obj.SetcanEate();

    def __init__(self, courier,prepareTime):
        self.canEate=0
        self.canEateTime=0
        self.HowlongToPrepare=prepareTime
        self.courier=courier
        self.courier.order = self
        self.waitTime=timedelta()
        Order.orders.append(self)
        self.trigger=RepeatedTimer(self.HowlongToPrepare,Order.OrdercanEate,self)
        self._key_lock = threading.Lock()

    def setWaitTime(self,now):
        assert self.courier.Arrived == 1
        self.waitTime = now - self.canEateTime
        self.getUpdateTime = now
        print('order waiting for courier:  %s s\n' % (str(self.waitTime.total_seconds()))) #if debugFlag == '1' else None

    def SetcanEate(self):
        now = datetime.now()
        with self._key_lock:
            self.canEate = 1
            self.canEateTime = now;
            if self.courier.Arrived == 1:
                self.courier.setWaitTime(now)
            else:
                assert self.courier.Arrived == 0


class Courier(object):
    couriers=[]
    @classmethod
    def CourierArrived(cls,obj):
        print('------------> Arrived %d taking %d prepareTime %d travelling %.3f s: '%(id(obj),id(obj.order),obj.order.HowlongToPrepare, obj.HowlongToArrive)) if debugFlag == '1' else None
        obj.trigger.stop()
        obj.SetArrived();

    def __init__(self):
        self.Arrived=0
        self.ArrivedTime=0
        self.HowlongToArrive=random.uniform(3,15)
        self.order=None
        self.waitTime=timedelta()
        Courier.couriers.append(self)
        self.seqNumber= len(Courier.couriers)
        self.trigger=RepeatedTimer(self.HowlongToArrive,Courier.CourierArrived,self)
        self._key_lock = threading.Lock()

    

    def setWaitTime(self,now):
        assert self.order.canEate == 1
        self.waitTime = now - self.ArrivedTime
        self.getUpdateTime = now
        print('Courier waiting for order: %s s\n' % (str(self.waitTime.total_seconds()))) #if debugFlag == '1' else None

    def SetArrived(self):
        now = datetime.now()
        with self._key_lock:
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

        
