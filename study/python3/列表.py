#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/11/10 22:23
'''Python有6个序列的内置类型，但最常见的是列表和元组。
序列都可以进行的操作包括索引，切片，加，乘，检查成员。'''
'''创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可。如下所示
与字符串的索引一样，列表索引从0开始。列表可以进行截取、组合等。'''
# list1 = ['Google', 'Runoob', 1997, 2000];
# list2 = [1, 2, 3, 4, 5 ];
# list3 = ["a", "b", "c", "d"];


'''访问列表中的值   使用下标索引来访问列表中的值，同样你也可以使用方括号的形式截取字符，如下所示：'''
# list1 = ['Google', 'Runoob', 1997, 2000];
# list2 = [1, 2, 3, 4, 5, 6, 7];
#
# print("list1[0]: ", list1[0])
# print("list2[1:5]: ", list2[1:5])


'''更新列表   你可以对列表的数据项进行修改或更新，你也可以使用append()方法来添加列表项，如下所示：'''
# list = ['Google', 'Runoob', 1997, 2000]
# print("第三个元素为 : ", list[2])
# list[2] = 2001
# print("更新后的第三个元素为 : ", list[2])

'''删除列表元素    可以使用 del 语句来删除列表的的元素，如下实例：'''
# list = ['Google', 'Runoob', 1997, 2000]
# print("原始列表 : ", list)
# del list[2]
# print("删除第三个元素 : ", list)

'''Python列表脚本操作符    列表对 + 和 * 的操作符与字符串相似。+ 号用于组合列表，* 号用于重复列表。'''

'''     len([1, 2, 3])	                         3	                         长度
       [1, 2, 3] + [4, 5, 6]	               [1, 2, 3, 4, 5, 6]	         组合
           ['Hi!'] * 4	                    ['Hi!', 'Hi!', 'Hi!', 'Hi!']	 重复
        3 in [1, 2, 3]	                              True	                 元素是否存在于列表中
        for x in [1, 2, 3]: print(x, end=" ")	   1 2 3	                  迭代'''


'''Python列表截取与拼接     Python的列表截取与字符串操作类型，如下所示：'''
# L=['Google', 'Runoob', 'Taobao']
# print(L[2])
# print(L[-2])
# print(L[1:])

# squares = [1, 4, 9, 16, 25]
# squares += [36, 49, 64, 81, 100]
# print(squares)

'''嵌套列表'''
# a = ['a', 'b', 'c']
# n = [1, 2, 3]
# x = [a, n]
# print(x)
# print(x[0])
# print(x[0][1])

'''len() 方法返回列表元素个数。
len()方法语法：len(list)'''
# list1 = ['Google', 'Runoob', 'Taobao']
# print (len(list1))
# list2=list(range(5)) # 创建一个 0-4 的列表
# print (len(list2))


'''count() 方法用于统计某个元素在列表中出现的次数
count()方法语法：list.count(obj)'''
# aList = [123, 'Google', 'Runoob', 'Taobao', 123];
# print ("123 元素个数 : ", aList.count(123))
# print ("Runoob 元素个数 : ", aList.count('Runoob'))

'''append() 方法用于在列表末尾添加新的对象。
append()方法语法：list.append(obj)'''
# list1 = ['Google', 'Runoob', 'Taobao']
# list1.append('Baidu')
# print ("更新后的列表 : ", list1)

'''extend() 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
extend()方法语法：list.extend(seq)'''
# list1 = ['Google', 'Runoob', 'Taobao']
# list2=list(range(5)) # 创建 0-4 的列表
# list1.extend(list2)  # 扩展列表
# print ("扩展后的列表：", list1)

'''reverse() 函数用于反向列表中元素
reverse()方法语法：list.reverse()'''
# list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
# list1.reverse()
# print ("列表反转后: ", list1)

'''sort() 函数用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数。
sort()方法语法：list.sort(cmp=None, key=None, reverse=False)
cmp -- 可选参数, 如果指定了该参数会使用该参数的方法进行排序。
key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）。'''
# aList = ['Google', 'Runoob', 'Taobao', 'Facebook']
# aList.sort()
# print("List : ", aList)

#以下实例降序输出列表：
# 列表
# vowels = ['e', 'a', 'u', 'o', 'i']
# # 降序
# vowels.sort(reverse=True)
# # 输出结果
# print('降序输出:', vowels)

#以下实例演示了通过指定列表中的元素排序来输出列表：
# 获取列表的第二个元素
# def takeSecond(elem):
#     return elem[1]
# # 列表
# random = [(2, 2), (3, 4), (4, 1), (1, 3)]
# # 指定第二个元素排序
# random.sort(key=takeSecond)
# # 输出类别
# print('排序列表：', random)

'''clear() 函数用于清空列表，类似于 del a[:]
clear()方法语法：list.clear()'''
# list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
# list1.clear()
# print ("列表清空后 : ", list1)


'''copy() 函数用于复制列表，类似于 a[:]
copy()方法语法：list.copy()'''
# list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
# list2 = list1.copy()
# print ("list2 列表: ", list2)

'''remove() 函数用于移除列表中某个值的第一个匹配项。
remove()方法语法：list.remove(obj)'''
list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
list1.remove('Taobao')
print ("列表现在为 : ", list1)
list1.remove('Baidu')
print ("列表现在为 : ", list1)