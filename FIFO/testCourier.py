# -*- coding: UTF-8 -*-
import unittest
import queue,time
from datetime import datetime,timedelta
from Courier import Courier,Order,debugFlag,OrdersPerSecond
class testCourier(unittest.TestCase):
    """docstring for testCourier"""
    def setUp(self):
        super(testCourier, self).setUp()
        self.courierArrivedQueue = queue.Queue()
        self.courier = Courier(self.courierArrivedQueue);
        pass

    def tearDown(self):
        pass

    def test_Init(self):
        self.assertEqual(self.courierArrivedQueue.qsize(),0)  

if __name__ == '__main__':
    unittest.main()
