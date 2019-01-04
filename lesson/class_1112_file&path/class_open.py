#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/11/25 10:14

'''mode的参数设置
r:只读read
w：只写write    如果文件存在，清空后再写    如果文件不存在，新建文件后再写
a:追加append   如果文件存在  不清空 直接添加内容 ；  如果文件不存在，新建文件后 直接添加内容
w模式和a模式都是只可写，不可读
r+：读写
w+：读写
a+：读写'''
'''读取全部的值'''
# file=open('python12.txt',encoding='utf-8')
# res=file.read()   #读取全部的值
# print("读取的结果是：{}".format(res))

'''读取指定个数的值'''
# file=open('python12.txt',encoding='utf-8')
# res=file.read(4)  #读取指定长度的内容  从最开始读取
# print("读取的结果是：{}".format(res))


# file=open('python12.txt',encoding='utf-8')
# res_1=file.read(4)
# res_2=file.read()  #接着在res_1的后面继续读
# print("1读取的结果是：{}".format(res_1))
# print("2读取的结果是：{}".format(res_2))

#
# file=open('python12.txt',encoding='utf-8')
# res_2=file.read()  #不传指定长度，就全部读完
# res_1=file.read(4)  #可以传入指定长度
# print("1读取的结果是：{}".format(res_1))
# print("2读取的结果是：{}".format(res_2))


# file=open('python12.txt',encoding='utf-8')
# res=file.readline()
# print("1读取的结果是：{}".format(res))  #读取第一行的内容

# file=open('python12.txt',encoding='utf-8')
# file.readline()
# res=file.readline()  #按行读取
# print("1读取的结果是：{}".format(res))   #读取第二行的内容

'''readlines()一次性读完所有的内容  返回是是列表'''
# file=open('python12.txt',encoding='utf-8')
# res=file.readlines()  #按行读取
# print("1读取的结果是：{}".format(res))

'''w模式  如果文件存在，清空后再写'''
# file = open('python12.txt', mode='w',encoding='utf-8')
# file.write("C组非常优秀")

'''w模式  如果文件不存在，新建文件后再写'''
# file = open('python13.txt', mode='w',encoding='utf-8')
# file.write("C组非常优秀")

'''a:追加append  文件存在  不清空 直接添加内容'''
# file = open('python13.txt', mode='a',encoding='utf-8')
# file.write('D组非常秀')

'''a:追加append  文件不存在，新建文件后 直接添加内容'''
# file = open('python14.txt', mode='a',encoding='utf-8')
# file.write('D组非常秀')

'''a模式不可读'''
# file = open('python14.txt', mode='a',encoding='utf-8')
# file.read()   #io.UnsupportedOperation: not readable

'''w模式不可读'''
# file = open('python14.txt', mode='w',encoding='utf-8')
# file.read()   #io.UnsupportedOperation: not readable

'''r+覆盖  先写后读，则会覆盖之后再读'''
# file = open('python14.txt', mode='r+',encoding='utf-8')
# file.write("大大姑娘")
# print(file.read())

'''r+覆盖  先读后写，会跟着鼠标光标移动，再在后面写'''
# file = open('python14.txt', mode='r+',encoding='utf-8')
# print(file.read())
# file.write("高一同学")

'''w+模式  文件存在 ，会清空'''
# file = open('python14.txt', mode='w+', encoding='utf-8')
# print(file.read())  #文件存在 ，会清空,读取不到内容
# file.write("大喜线儿")


# file = open('python14.txt', mode='w+', encoding='utf-8')
# file.write("萌萌哒")  #写入萌萌哒
# print(file.read())  #读取不到内容

'''w+模式   utf-8  一个汉字3个字节'''
# file = open('python14.txt', mode='w+', encoding='utf-8')
# file.write("萌萌哒小米flora")  #写入萌萌哒
# print(file.tell())#获取当前光标位置
# print(file.readline())

'''seek(offset,[from])方法改变当前文件的位置，
offset变量表示要移动的位数，from变量指定开始移动字节的参考位置
0：参考位置为文件开头
1：参考位置设为当前所在位置
2：参考位置设为文件结尾'''
# file = open('python14.txt', mode='w+', encoding='utf-8')
# file.write("长大就是这样")
# print(file.tell())#获取当前光标位置
# file.seek(0,0) #位移之后 获取光标位置
# print(file.tell())#获取你当前的光标位置
# print(file.readline())

'''a+追加'''
file = open('python14.txt', mode='a+', encoding='utf-8')
file.write("十二")
print(file.tell())#获取当前光标位置
file.seek(0,0) #位移之后 获取光标位置
print(file.tell())#获取你当前的光标位置
print(file.readline())