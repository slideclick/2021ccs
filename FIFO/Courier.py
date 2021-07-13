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
        obj.q.put(obj)
        print('----> canEate: %d after %d prepareTime'%( id(obj),obj.HowlongToPrepare)) if debugFlag == '1' else None
        obj.SetcanEate();

    def __init__(self, prepareTime,q):
        self.canEate=0
        self.canEateTime=0
        self.deQueueTime = 0
        self.HowlongToPrepare=2#prepareTime
        self.waitTime=timedelta()
        Order.orders.append(self)
        self.trigger=RepeatedTimer(self.HowlongToPrepare,Order.OrdercanEate,self)
        self.q=q

    def SetcanEate(self):
        now = datetime.now()
        self.canEate = 1
        self.canEateTime = now;

    def SetPicked(self,now):
        self.waitTime = now - self.canEateTime
        self.deQueueTime = now 
        


class Courier(object):
    couriers=[]
    @classmethod
    def CourierArrived(cls,obj):
        obj.trigger.stop()
        obj.q.put(obj)
        print('------------> Arrived %d after travelling %.3f s: '%(id(obj), obj.HowlongToArrive)) if debugFlag == '1' else None
        obj.SetArrived();

    def __init__(self, q):
        self.Arrived=0
        self.ArrivedTime=0
        self.deQueueTime = 0
        self.HowlongToArrive= 5#random.uniform(3,15)
        self.waitTime=timedelta()
        Courier.couriers.append(self)
        self.trigger=RepeatedTimer(self.HowlongToArrive,Courier.CourierArrived,self)
        self.q=q

    def SetArrived(self):
        now = datetime.now()
        self.Arrived = 1
        self.ArrivedTime = now;
        
    def SetPicked(self,now):
        self.waitTime = now - self.ArrivedTime
        self.deQueueTime = now 


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    pass        

        
