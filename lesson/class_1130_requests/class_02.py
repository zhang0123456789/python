#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/12/1 11:38
import requests

#发送get请求
# url='http://www.lemfix.com/topics/25'
# res=requests.get(url)
# print(res)    #返回结果为对象

'''response里面包含响应头、响应正文、状态码'''

'''响应头'''
# url='http://www.lemfix.com/topics/25'
# res=requests.get(url)
# print(res.headers)
'''响应正文'''
# url='http://www.lemfix.com/topics/25'
# res=requests.get(url)
# print(res.text)
'''状态码'''
# url='http://www.lemfix.com/topics/25'
# res=requests.get(url)
# print(res.status_code)


'''request里面包含 请求头 请求正文  请求方式  url '''

'''请求头'''
# url='http://www.lemfix.com/topics/25'
# res=requests.get(url)
# print(res.request.headers)
'''请求地址'''
# url='http://www.lemfix.com/topics/25'
# res=requests.get(url)
# print(res.url)


