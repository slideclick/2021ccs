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
        print('----> canEate: %d after %d prepareTime'%( id(obj),obj.HowlongToPrepare)) if debugFlag == '1' else None
        obj.SetcanEate();
        obj.q.put(obj)

    def __init__(self, prepareTime,q):
        self.canEate=0
        self.canEateTime=datetime(1,1,1)
        self.deQueueTime = 0
        self.HowlongToPrepare=2#prepareTime
        self.waitTime=timedelta()
        Order.orders.append(self)
        self.trigger=RepeatedTimer(self.HowlongToPrepare,Order.OrdercanEate,self)
        self.q=q

    def SetcanEate(self):
        self.canEate = 1
        self.canEateTime = datetime.now();
        print("SetcanEate: ",self.__class__,self.canEateTime)if debugFlag == '1' else None

    def SetPicked(self,current):
        print(type(current),current,self.canEateTime)
        self.waitTime = current - self.canEateTime
        self.deQueueTime = current 
        print('%s %d waittime %.3f'%(self.__class__,id(self),self.waitTime.total_seconds()))      


class Courier(object):
    couriers=[]
    @classmethod
    def CourierArrived(cls,obj):
        obj.trigger.stop()
        print('------------> Arrived %d after travelling %.3f s: '%(id(obj), obj.HowlongToArrive)) if debugFlag == '1' else None
        obj.SetArrived();
        obj.q.put(obj)

    def __init__(self, q):
        self.Arrived=0
        self.ArrivedTime=datetime(1,1,1)
        self.deQueueTime = 0
        self.HowlongToArrive= 5#random.uniform(3,15)
        self.waitTime=timedelta()
        Courier.couriers.append(self)
        self.trigger=RepeatedTimer(self.HowlongToArrive,Courier.CourierArrived,self)
        self.q=q

    def SetArrived(self):
        self.Arrived = 1
        self.ArrivedTime = datetime.now();
        print("SetArrived: ",self.__class__,type(self.ArrivedTime))if debugFlag == '1' else None

    def SetPicked(self,now):
        print(type(now),now,self.ArrivedTime)
        self.waitTime = now - self.ArrivedTime
        self.deQueueTime = now 
        print('%s %d waittime %.3f'%(self.__class__,id(self),self.waitTime.total_seconds()))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    pass        

        
