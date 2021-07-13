# -*- coding: UTF-8 -*-
import unittest

from datetime import datetime,timedelta
from Courier import Courier,Order,debugFlag,OrdersPerSecond

class testCourier(unittest.TestCase):
    """docstring for testCourier"""

    def setUp(self):
        super(testCourier, self).setUp()
        self.courier = Courier();
        pass

    def tearDown(self):
        pass


    def testInit(self):
        self.assertEqual(self.courier.Arrived,0) 

if __name__ == '__main__':
    unittest.main()
