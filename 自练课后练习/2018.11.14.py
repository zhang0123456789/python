#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2018/11/14 21:48
'''有如下值集合 [11,22,33,44,55,66,77,88,99,90]，
将所有大于 66 的值保存至字典的第一个 key 中，
将小于 66 的值保存至第二个 key 的值中。
即： {'k1': 大于 66 的所有值,'k2': 小于 66 的所有值}'''

# list_1=[11,22,33,44,55,66,77,88,99,90]
# L1=[]
# L2=[]
# for i in list_1:
#     if i >66:
#         L1.append(i)
#     else:
#         L2.append(i)
# dict={"K1":L1,"K2":L2}
# print(dict)

'''.Pyhton 单行注释和多行注释分别用什么?'''
#单行注释#代码
#多行注释  '''代码'''     pycharm快捷键Ctrl+/?

'''九九乘法表'''
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("{}*{}={}".format(i,j,i*j),end=' ')
#     print()

# a=1
# while a<=9:
#     b=0
#     while b<a:
#         b+=1
#         print("{}*{}={}".format(a,b,a*b),end=' ')
#     a += 1
#     print()

'''15.字符串: a = ‘abcd’, 用2个方法取出字母d'''
a='abcd'
#1、print(a[3])
#2、print(a[-1])
#3、b=list(a)
#   print(b.pop())


'''列表a = [1,2,3,4,5]
(1).用2种方法输出下面的结果：[1,2,3,4,5,6,7,8]'''
# a=[1,2,3,4,5]
# b=[6,7,8]
# print(a+b)

# b=[1,2,3,4,5]
# b.extend([6,7,8])
# print(b)
'''用列表的2种方法返回结果：[5,4]'''
# b=a[-1:-3:-1]
# print(b)

# a=[1,2,3,4,5]
# c=[]
# c.append(a.pop())
# c.append(a.pop())
# print(c)

'''(3).判断2是否在列表里'''
a = ([1,2,3,4,5])
if 2 in a:
    print(True)
else:
    print(False)
