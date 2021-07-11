# -*- coding: UTF-8 -*-
from Config import ConfigParser
from Courier import Courier
from Order import Order
import queue,sys
import time
import threading

box=15
class GoodsConsume(threading.Thread):
    def __init__(self,q):
        super(GoodsConsume,self).__init__()
        self.queuelist=q

    def run(self):
        while True:
            if not self.queuelist.empty():
                event=self.queuelist.get()
                print( "%s , obj %d,box have :%d" % (event.__class__, id(event),self.queuelist.qsize()))
                
            else :
                time.sleep(0.5)
                if  self.queuelist.empty():
                   pass#print( "NOTE: BOX is null ,please wait ...  size %d ,fillin 0" % (box))

            time.sleep(0.5)
    def show(self):
        print ("GoodsConsume %s ,infomation -- %d"%(self.__class__,self.queuelist.qsize()))


def GetNextOrder(q):
    courier = Courier(q);
    o=Order(courier);
    courier.Order = o
    return o

if __name__ == '__main__':
    print(ConfigParser.config_dic)
    try:
        eventQueue = queue.Queue()
        c=GoodsConsume(eventQueue)
        c.start()
        c.show()
        for i in range(3):
            print(i)
            GetNextOrder(eventQueue)
            time.sleep(0.5)
    except KeyboardInterrupt:
        print ("interrupt")
        sys.exit(1)
    print('exit')