# -*- coding: UTF-8 -*-
from Config import ConfigParser
from Courier import Courier,Order,debugFlag,OrdersPerSecond

import time,json
import queue,sys,statistics 
import threading

# box=15
# class GoodsConsume(threading.Thread):
#     def __init__(self,q):
#         super(GoodsConsume,self).__init__()
#         self.queuelist=q

#     def run(self):
#         while True:
#             if not self.queuelist.empty():
#                 event=self.queuelist.get()
#                 print( "%s , obj %d,box remained :%d" % (event.__class__, id(event),self.queuelist.qsize()))
                
#             else :
#                 time.sleep(0.5)

#             time.sleep(0.5)
#     def show(self):
#         print ("GoodsConsume %s ,infomation -- %d"%(self.__class__,self.queuelist.qsize()))


def GetNextOrder(prepareTime,orderDoneQueue,courierArrivedQueue):
    courier = Courier(courierArrivedQueue);
    o=Order(prepareTime,orderDoneQueue);
    return o

if __name__ == '__main__':
    try:
        orderDoneQueue = queue.Queue()
        courierArrivedQueue = queue.Queue()
        with open('sample.json',encoding='utf-8') as f_in: #sample
            data = json.load(f_in)
            for seq,order in enumerate(data):
                prepareTime = int (order['prepTime'])
                print('Order %d new with prepareTime: %d'%(seq+1,prepareTime)) 
                GetNextOrder(prepareTime,orderDoneQueue,courierArrivedQueue)
                time.sleep(1/int(OrdersPerSecond))# 2 order per second by default

        while True:
            if not ( all(x.canEate==1 for x in Order.orders) and all(x.Arrived == 1 for x in Courier.couriers) ):
                print('qsize down: ',len([x.canEate for x in Order.orders if x.canEate==0]))  if debugFlag == '1' else None            
            else:
                print('Order   Average  Waittime(seconds): %.3f ,total %d orders' % (statistics.mean([x.waitTime.total_seconds() for x in Order.orders]),len(Order.orders)))
                print('Courier Average  Waittime(seconds): %.3f ,total %d courier' % (statistics.mean([x.waitTime.total_seconds() for x in Courier.couriers]),len(Courier.couriers)))
                print()
                break
            time.sleep(3)
    except KeyboardInterrupt:
        print ("interruptted by Ctrl-c")

    print('main thread exit')  