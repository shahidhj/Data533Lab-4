import unittest
from Testing_User.test_Teacher import  MyTeacherTest
from Testing_User.test_Student import MyTestStudent


def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(MyTestStudent))
    suite.addTest(unittest.makeSuite(MyTeacherTest))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))

my_suite()



