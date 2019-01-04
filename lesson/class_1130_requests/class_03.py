#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/12/1 11:55
import requests
'''登录'''
# login='http://47.107.168.87:8080/futureloan/mvc/api/member/login'
# login_data={'mobilephone':18688773467,'pwd':'123456'}
# login_res=requests.get(login,login_data)#发送一个get请求
# print(login_res.text)#查看响应正文
# print(login_res.status_code)#状态码
# print(login_res.cookies)#cookies:登录成功之后
# print(login_res.cookies['JSESSIONID'])#cookies 类字典的形式
# '''登录成功后，发起充值请求'''
# recharge='http://47.107.168.87:8080/futureloan/mvc/api/member/recharge'
# recharge_data={'mobilephone':18688773467,'amount':'1000'}
# recharge_res=requests.post(recharge,recharge_data,cookies=login_res.cookies)
# print(recharge_res.json())
'''text  json
你们返回的响应正文不管是什么内容 都可以用text获取
如果你们返回的响应正文是 字典格式、 json格式的json获取'''
'''1、什么时候带cookies？  如果这个请求需要在用户登录成功之后才能操作就需要带cookies'''
'''2、text json都可以获取结果  我用那个比较好  如果你要取值的话，建议用字典'''
'''3、'''


'''用text获取的是字符串'''
login='http://47.107.168.87:8080/futureloan/mvc/api/member/login'
login_data={'mobilephone':18688773467,'pwd':'123456'}
login_res=requests.get(login,login_data)#发送一个get请求
print(login_res.text)
print('login_res.text',type(login_res.text))  #返回类型为str
'''用json获取的是字典'''
print('-'*100)  #分割线
recharge='http://47.107.168.87:8080/futureloan/mvc/api/member/recharge'
recharge_data={'mobilephone':18688773467,'amount':'1000'}
recharge_res=requests.post(recharge,recharge_data,cookies=login_res.cookies)
print(recharge_res.json())
print(recharge_res.json()['msg'])   #字典取值
print('recharge_res.json():',type(recharge_res.json()))  #返回字典格式
