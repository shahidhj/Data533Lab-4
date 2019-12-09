# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 17:49:52 2019

@author: Ritayu_Nagpal
"""

import unittest
from Testing_Inventory.test_literature import TestLiterature
from Testing_Inventory.test_stationary import TestStationary
from Testing_User.test_Teacher import  MyTeacherTest
from Testing_User.test_Student import MyTestStudent


def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestLiterature))
    suite.addTest(unittest.makeSuite(TestStationary))
    suite.addTest(unittest.makeSuite(MyTestStudent))
    suite.addTest(unittest.makeSuite(MyTeacherTest))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))
my_suite()