# -*- coding: utf-8 -*-
# @Time    : 2018/12/10 20:29
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : project_path.py
#专门来存储我们路径的变量
import os

base_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
print(base_path)
#想得到配置文件的路径
config_path=os.path.join(base_path,'conf','test_api.conf')
print(config_path)
#测试报告的路径
report_path=os.path.join(base_path,'test_result','report','test_api.html')

#日志的路径
log_path=os.path.join(base_path,'test_result','log','test_api.txt')

#测试用例的路径
case_path=os.path.join(base_path,'test_case','test_cases.xlsx')

