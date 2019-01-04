#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/12/1 12:52
import requests
#小要求：请写一个函数  可以完成任何http的get请求或是post请求

def http_request(url,param,http_method,cookie=None):
    if http_method=='get':
        res=requests.get(url,param,cookies=cookie)
    else:
        res=requests.post(url,param,cookies=cookie)
    return  res
if __name__=='__main__':
    '''登录'''
    login='http://47.107.168.87:8080/futureloan/mvc/api/member/login'
    login_data={'mobilephone': 18688773467, 'pwd': '123456'}
    '''充值'''
    recharge='http://47.107.168.87:8080/futureloan/mvc/api/member/recharge'
    recharge_data={'mobilephone': 18688773467, 'amount': '1000'}
    res_login=http_request(login,login_data,'get')
    print('登录的结果：',res_login.json())
    print('_'*150)
    res_recharge=http_request(recharge,recharge_data,'post',cookie=res_login.cookies)
    print('充值的结果：',res_recharge.json())

