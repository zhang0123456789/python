#encoding=utf-8
__author__ = 'Administrator'
'''
@Time:2018-12-2 16:38
'''
import unittest
import HTMLTestRunnerNew
from python12_HomeWork_1130.Unitesttest import UnitestTest

class ExcuteTestCase:
    def doRequest(self):
        login='http://47.107.168.87:8080/futureloan/mvc/api/member/login'
        login_data={'mobilephone':18688773467,'pwd':'123456'}
        recharge='http://47.107.168.87:8080/futureloan/mvc/api/member/recharge'
        recharge_data={'mobilephone':18688773467,'amount':'1000'}
        suite=unittest.TestSuite()
        suite.addTest(UnitestTest(login,login_data,"get","test_login"))
        suite.addTest(UnitestTest(recharge,recharge_data,"post","test_recharge"))
        with open("Python12.html","wb+") as file:
            runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2,title="Python12",description="request测试",tester="兵心")
            runner.run(suite)
if __name__ == '__main__':
    ExcuteTestCase().doRequest()
