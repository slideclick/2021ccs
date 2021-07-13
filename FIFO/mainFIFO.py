# -*- coding: UTF-8 -*-
from Config import ConfigParser
from Courier import Courier,Order,debugFlag,OrdersPerSecond
from datetime import datetime,timedelta
import time,json
import queue,sys,statistics 
import threading

class Dispactcher(threading.Thread):
    def __init__(self,orderQueue,courierQueue):
        super(Dispactcher,self).__init__()
        self.orderQueue=orderQueue
        self.courierQueue=courierQueue

    def run(self):
        while True:
            order = self.orderQueue.get()
            if order:
                courier = self.courierQueue.get()
                now=  datetime.now()
                if courier:
                    courier.SetPicked(now);
                    order.SetPicked(now);

                    print( "%s obj %d picked by %d,queue remained :%d" % (order.__class__, id(order),id(courier),self.orderQueue.qsize()))
                
            else :
                pass
            
    def show(self):
        print ("Dispactcher %s ,infomation -- %d"%(self.__class__,self.orderQueue.qsize()))if debugFlag == '1' else None


def GetNextOrder(prepareTime,orderDoneQueue,courierArrivedQueue):
    courier = Courier(courierArrivedQueue);
    o=Order(prepareTime,orderDoneQueue);
    return o

if __name__ == '__main__':
    try:
        orderDoneQueue = queue.Queue()
        courierArrivedQueue = queue.Queue()
        c=Dispactcher(orderDoneQueue,courierArrivedQueue)
        c.start()
        c.show()
        with open('sample.json',encoding='utf-8') as f_in: #sample
            data = json.load(f_in)
            for seq,order in enumerate(data):
                prepareTime = int (order['prepTime'])
                print('Order %d new with prepareTime: %d'%(seq+1,prepareTime)) 
                GetNextOrder(prepareTime,orderDoneQueue,courierArrivedQueue)
                time.sleep(1/int(OrdersPerSecond))# 2 order per second by default

        while True:
            if not ( all(x.canEate==1 for x in Order.orders) and all(x.Arrived == 1 for x in Courier.couriers) ):
                pass#print('qsize down: ',len([x.canEate for x in Order.orders if x.canEate==0]))  if debugFlag == '1' else None            
            else:
                print('Order   Average  Waittime(seconds): %.3f ,total %d orders' % (statistics.mean([x.waitTime.total_seconds() for x in Order.orders]),len(Order.orders)))
                print('Courier Average  Waittime(seconds): %.3f ,total %d courier' % (statistics.mean([x.waitTime.total_seconds() for x in Courier.couriers]),len(Courier.couriers)))
                print()
                break
            time.sleep(3)
    except KeyboardInterrupt:
        print ("interruptted by Ctrl-c")

    print('main thread exit')  