# -*- coding: UTF-8 -*-
import unittest

from datetime import datetime,timedelta
from Config import ConfigParser

class testConfig(unittest.TestCase):
    """docstring for testConfig"""

    def setUp(self):
        super(testConfig, self).setUp()
        self.con = ConfigParser();
        pass

    def tearDown(self):
        pass


    def testGetValue(self):
        res=self.con.get_config('basic', 'OrdersPerSecond')
        self.assertEqual(res,'2') 

if __name__ == '__main__':
    unittest.main()
