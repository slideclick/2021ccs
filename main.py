# -*- coding: UTF-8 -*-

from Courier import Courier,Order,debugFlag,OrdersPerSecond
import queue,sys,statistics 
import time
import threading


def GetNextOrder():
    courier = Courier();
    o=Order(courier);
    return o

if __name__ == '__main__':

    try:
        for i in range(10):
            print('Order: %d'%i)
            GetNextOrder()
            time.sleep(1/int(OrdersPerSecond))# 2 order per second by default

        while True:
            if not ( all(x.canEate==1 for x in Order.orders) and all(x.Arrived == 1 for x in Courier.couriers) ):
                print('qsize down: ',len([x.canEate for x in Order.orders if x.canEate==0])) # if debugFlag == '1' else None            
            else:
                print('Order   Average  Waittime(seconds): %.3f' % statistics.mean([x.waitTime.total_seconds() for x in Order.orders]))
                print('Courier Average  Waittime(seconds): %.3f' % statistics.mean([x.waitTime.total_seconds() for x in Courier.couriers]))
                print()
            time.sleep(3)
    except KeyboardInterrupt:
        print ("interruptted by Ctrl-c")
        sys.exit(1)            
