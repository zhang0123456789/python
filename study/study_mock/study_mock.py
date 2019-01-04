#!/usr/bin/env python
# -*- coding:utf-8-*-
#@author:蜜蜜
#@file: study_mock.py 
#@time: 2018/12/26 
#@email:1402686685@qq.com
'''unittest.mock是一个用于在Python中进行单元测试的库，Mock翻译过来就是模拟的意思，
顾名思义这个库的主要功能是模拟一些东西。
它的主要功能是使用mock对象替代掉指定的Python对象，以达到模拟对象的行为。'''

'''1.如下场景：支付是一个独立的接口，由其它开发提供，
，还是成功，这个是你需要实现的功能
也就是说你写一个b功能，你的同事写一个a功能，
，然后实现对应的功能。这就是存在依赖关系，
你同事开发的进度你是无法控制的
你要是等他开发完了，你再开发，那你就坐等加班吧.'''


from unittest import mock
import unittest
from study.study_mock import temple

class Test_zhifu_statues(unittest.TestCase):
    '''单元测试用例'''
    def test_01(self):
        '''测试支付成功场景'''
        # mock一个支付成功的数据
        temple.zhifu = mock.Mock(return_value={"result": "success", "reason":"null"})
        # 根据支付结果测试页面跳转
        statues = temple.zhifu_statues()
        print(statues)
        self.assertEqual(statues, "支付成功")

    def test_02(self):
        '''测试支付失败场景'''
        # mock一个支付成功的数据
        temple.zhifu = mock.Mock(return_value={"result": "fail", "reason": "余额不足"})
        # 根据支付结果测试页面跳转
        statues = temple.zhifu_statues()
        self.assertEqual(statues, "支付失败")

if __name__ == "__main__":
    unittest.main()