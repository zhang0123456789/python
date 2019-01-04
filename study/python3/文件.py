#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/11/13 7:18
'''open() 方法
Python open() 方法用于打开一个文件，并返回文件对象，
在对文件进行处理过程都需要使用到这个函数，如果该文件无法被打开，会抛出 OSError。'''

'''注意：使用 open() 方法一定要保证关闭文件对象，即调用 close() 方法。'''

'''open() 函数常用形式是接收两个参数：文件名(file)和模式(mode)。
open(file, mode='r')'''

# # 打开文件
# fo = open("runoob.txt", "wb")
# print("文件名为: ", fo.name)
# # 关闭文件
# fo.close()

'''Python 3 中的 File 对象不支持 next() 方法。 Python 3 的内置函数 next() 通过迭代器调用 __next__() 方法返回下一项。 在循环中，
next()方法会在每次循环中调用，该方法返回文件的下一行，如果到达结尾(EOF),则触发 StopIteration'''

# 打开文件
fo = open("runoob.txt", "r")
print ("文件名为: ", fo.name)

for index in range(5):
    line = next(fo)
    print ("第 %d 行 - %s" % (index, line))

# 关闭文件
fo.close()