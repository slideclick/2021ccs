# -*- coding: UTF-8 -*-
from Config import ConfigParser
from Courier import Courier
from Order import Order
import queue,sys
import time

def GetNextOrder(q):
    courier = Courier(q);
    o=Order(courier);
    courier.Order = o
    return o

class Events(object):
    """docstring for Events"""
    def __init__(self, name,data):
        self.name = name
        self.data=data

if __name__ == '__main__':

    print(ConfigParser.config_dic)
    
       
    try:
        eventQueue = queue.Queue()
        for i in range(3):
            print(i)
            GetNextOrder(eventQueue)
            time.sleep(0.5)
            print(i)
            while not eventQueue.empty():
                print(eventQueue.get(), end=' ')
            print()
    except KeyboardInterrupt:
        print ("interrupt")
        sys.exit(1)
    print()