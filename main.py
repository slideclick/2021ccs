# -*- coding: UTF-8 -*-

from Courier import Courier,Order,debugFlag,OrdersPerSecond
import queue,sys,statistics 
import time,json
import threading


def GetNextOrder(prepareTime):
    courier = Courier();
    o=Order(courier,prepareTime);
    return o

if __name__ == '__main__':

    try:
        with open('dispatch_orders.json',encoding='utf-8') as f_in: #sample
            data = json.load(f_in)
            for order in data:
                prepareTime = int (order['prepTime'])
                print('Order new with prepareTime: %d'%prepareTime) 
                GetNextOrder(prepareTime)
                time.sleep(1/int(OrdersPerSecond))# 2 order per second by default

        while True:
            if not ( all(x.canEate==1 for x in Order.orders) and all(x.Arrived == 1 for x in Courier.couriers) ):
                print('qsize down: ',len([x.canEate for x in Order.orders if x.canEate==0]))  if debugFlag == '1' else None            
            else:
                print('Order   Average  Waittime(seconds): %.3f ,total %d orders' % (statistics.mean([x.waitTime.total_seconds() for x in Order.orders]),len(Order.orders)))
                print('Courier Average  Waittime(seconds): %.3f ,total %d courier' % (statistics.mean([x.waitTime.total_seconds() for x in Courier.couriers]),len(Courier.couriers)))
                print()
            time.sleep(3)
    except KeyboardInterrupt:
        print ("interruptted by Ctrl-c")
        sys.exit(1)            
