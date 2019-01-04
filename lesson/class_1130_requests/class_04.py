#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/12/1 12:41
import requests
'''登录'''
login='http://47.107.168.87:8080/futureloan/mvc/api/member/login'
login_data={'mobilephone':18688773467,'pwd':'123456'}
'''充值'''
recharge='http://47.107.168.87:8080/futureloan/mvc/api/member/recharge'
recharge_data={'mobilephone':18688773467,'amount':'1000'}
#生成一个会话   同一个会话下，就不用传cookies
s=requests.session()
res_login=s.get(login,params=login_data)
res_recharge=s.get(recharge,params=recharge_data)
print('登录的结果：',res_login.json())
print('_'*150)
print('充值的结果：',res_recharge.json())