#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/11/10 23:14
'''Python 的元组与列表类似，不同之处在于元组的元素不能修改。
元组使用小括号，列表使用方括号。
元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。'''
# tup1 = ('Google', 'Runoob', 1997, 2000);
# tup2 = (1, 2, 3, 4, 5 );
# tup3 = "a", "b", "c", "d";   #  不需要括号也可以
# print(type(tup3))


'''创建空元组    tup1 = ();'''
'''元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用：'''
# tup1 = (50)
# print(type(tup1) ) # 不加逗号，类型为整型
#
# tup1 = (50,)
# print(type(tup1))  # 加上逗号，类型为元组

'''元组与字符串类似，下标索引从0开始，可以进行截取，组合等。'''
'''访问元组   元组可以使用下标索引来访问元组中的值，如下实例:'''
# tup1 = ('Google', 'Runoob', 1997, 2000)
# tup2 = (1, 2, 3, 4, 5, 6, 7)
# print("tup1[0]: ", tup1[0])
# print("tup2[1:5]: ", tup2[1:5])


'''修改元组
元组中的元素值是不允许修改的，但我们可以对元组进行连接组合，如下实例:'''
# tup1 = (12, 34.56);
# tup2 = ('abc', 'xyz')
# # 以下修改元组元素操作是非法的。
# # tup1[0] = 100
# # 创建一个新的元组
# tup3 = tup1 + tup2;
# print(tup3)

'''删除元组   元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组，如下实例:'''

'''en(tuple)  计算元组元素个数。'''
# tuple1 = ('Google', 'Runoob', 'Taobao')
# print( len(tuple1))

'''	max(tuple)   返回元组中元素最大值'''
# tuple2 = ('5', '4', '8')
# print( max(tuple2))

'''tuple(seq)   将列表转换为元组。'''
list1= ['Google', 'Taobao', 'Runoob', 'Baidu']
tuple1=tuple(list1)
print(tuple1)
