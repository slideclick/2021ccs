# -*- coding: UTF-8 -*-
import unittest

class testCourierddd(unittest.TestCase):
    """docstring for testCourier"""
    print(__name__)
    def __init__(self, arg):
        super(testCourier, self).__init__()
        self.arg = arg
    def setUp(self):
        pass

    def tearDown(self):
        pass



if __name__ == '__main__':
    unittest.main()
