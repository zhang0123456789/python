#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/11/30 21:28

'''http类型的请求  requests模块'''
import  requests
'''1、发送一个get类型请求  返回一个消息实体'''
# url='http://www.lemfix.com/topics/25'
# res=requests.get(url)
# print(res)   #返回<Response [200]>

'''2、发送一个post类型请求'''
# url='http://www.lemfix.com/topics/25'
# res_2=requests.post(url)
# print(res_2)   #返回<Response [404]>
'''二者返回值不同，说明不支持Post请求'''
# url='http://www.lemfix.com/topics/25'
# res=requests.get(url)
# print(res)   #返回<Response [200]>

'''默认传给data'''
# url='http://www.lemfix.com/topics/25'
# res_2=requests.post(url,data='a')
# print(res_2)


'''指定传给json'''
# url='http://www.lemfix.com/topics/25'
# res_2=requests.post(url,json={a})
# print(res_2)

'''默认传值'''
# def add (a,b=None,c=None):
#     print('a的值：',a)
#     print('b的值：',b)
#     print('c的值：',c)
# add(1,2)

'''指定赋值'''
# def add (a,b=None,c=None):
#     print('a的值：',a)
#     print('b的值：',b)
#     print('c的值：',c)
# add(1,c=2)

'''传俩种格式的数据，字典格式的赋值给data,json格式的赋值给json'''
url='http://www.lemfix.com/topics/25'
res_1=requests.get(url)
print(res_1)


'''俩种发送get请求的方式'''
# url='http://www.lemfix.com/topics/25'
# res_1=requests.get(url)
# print(res_1)
# url='http://www.lemfix.com/topics/25'
# res_2=requests.request('get',url)
# print(res_2)


'''俩种发送post请求的方式'''
# url='http://www.lemfix.com/topics/25'
# res_1=requests.post(url)
# print(res_1)
# url='http://www.lemfix.com/topics/25'
# res_2=requests.request('post',url)
# print(res_2)

