#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/11/13 7:32
import os
#E:\python_study\class\class07.py

'''新建目录   支持相对路径 支持绝对路径  当前你写的代码的这个文件相对'''
# os.mkdir("python12")  #新建在当前目录下面 生成的文件夹 相对路径
# os.mkdir("E:\python_study\class/python12")

''' 删除目录  支持相对路径 支持绝对路径   当前你写的代码的这个文件相对'''
# os.rmdir("python12")

'''建立多级目录  不可以跳着越级新建'''
# os.mkdir("python12")
# os.mkdir("python12/a")

'''删除包含有子文件夹的目录   不可以跨级删除'''
# os.rmdir("python12")

#怎么获取路劲的值
'''获取当前的工作目录  具体到目录'''
# path=os.getcwd()
# print(path)
'''获取当前的工作路劲  具体当文件'''
# path_2=os.path.realpath(__file__)
# print(path_2)




#在class下面建立python12目录  在python12在建立A目录  在A目录里面键b.txt文件
#如何获取python12文件夹下面子文件夹A的b.txt
#方法一：绝对路径  NO
#方法二：相对路径  NO


'''os.getcwd():getcwd()方法显示当前的工作路劲。只具体到路径  不具体到方法'''
#方法三：get.cwd  OK
#第一种方法：E:\python_study\class\python12\A\b.txt
# cwd_path=os.getcwd()
# txt_path=cwd_path+"/python12/A/b.txt"
# print(txt_path)

#方法四  ：realpath   OK
# real_path=os.path.realpath(__file__)
# print(real_path)
# print(os.path.split(real_path))  #返回元组
# print(os.path.split(real_path)[0])
# print(os.path.split(real_path)[0]+"//python12/A/b.txt")
# print(os.path.split(os.path.split(real_path)[0]))

'''os.listdir():获取当前路径下的目录列表    返回列表格式数据'''

#判断当前路径到底是目录还是文件   directory file
# print(os.path.isdir(real_path))  #判断是否问目录   返回布尔值
# print(os.path.isfile(real_path))  #判断是否为文件  返回布尔值
# print(os.listdir(os.path.split(real_path)[0]))#传入目录的文件

'''os.path.dirname(path)：返回文件路径
   os.path.basename(path):返回文件名'''
# print(real_path)
# print(os.path.dirname(real_path))
# print(os.path.basename(real_path))
# print(os.path.basename(__file__))


#拼接的路径的函数  os.path.join
# path=os.getcwd()
# new_path=os.path.join(path,"python13")
# print(new_path)
#
# path=os.getcwd()
# new_path=os.path.join(path,"python13","B")
# print(new_path)
#
# path=os.getcwd()
# new_path=os.path.join(path,"python13","B","1")
# print(new_path)
#
# path=os.getcwd()
# new_path=os.path.join(path,"python13/B/1")
# print(new_path)

# file=open("python12.txt")#读取txt中的英文
# '''mode的参数设置
# r:只读read
# 只写write  文件已经存在清空文件后再写,文件不存在，就会新建一个文件'''
# res=file.read()
# print("读取的结果时：{}".format(res))

# file=open("python12.txt",encoding='utf-8')#读取txt中含中文  加入编码格式
# '''mode的参数设置
# r:只读read
# 只写write  文件已经存在清空文件后再写,文件不存在，就会新建一个文件'''
# res=file.read()
# print("读取的结果时：{}".format(res))

# file=open("python12.txt",encoding='utf-8')#读取txt中含中文  加入编码格式
# '''mode的参数设置  文件不存在  则新建 再写入内容
# r:只读read  r+读写、覆盖   w+读写  a+  读写
# w:只写write  文件已经存在清空文件后再写,文件不存在，就会新建一个文件'''
# a:追加  append  追加内容  文件不存在则新建文件再写

# res=file.read(1)
# print("读取的结果时：{}".format(res))  #读取第一行

# file=open("python12.txt",encoding='utf-8')#读取txt中含中文  加入编码格式
# '''mode的参数设置
# r:只读read
# w:只写write  文件已经存在清空文件后再写,文件不存在，就会新建一个文件'''
# res=file.read(1)  #read()里面是长度
# print("读取的结果时：{}".format(res)) #从头开始读取

# file=open("python12.txt",encoding='utf-8')#读取txt中含中文  加入编码格式
# '''mode的参数设置
# r:只读read
# w:只写write  文件已经存在清空文件后再写,文件不存在，就会新建一个文件'''
# res=file.read(2)  #read()里面是长度
# print("读取的结果时：{}".format(res)) #从头开始读取

# file=open("python12.txt",encoding='utf-8')#读取txt中含中文  加入编码格式
# '''mode的参数设置
# r:只读read
# w:只写write  文件已经存在清空文件后再写,文件不存在，就会新建一个文件'''
# res=file.read(4)  #read()里面是长度
# print("读取的结果时：{}".format(res)) #从头开始读取

# file = open("python12.txt", encoding='utf-8')
# res=file.read(4)  #传入指定长度的内容
# res_2=file.read()  #不传长度就是全部读完
# print("1读取的结果是：{}".format(res))
# print("2读取的结果是：{}".format(res_2)) #读取完后就接着读

'''readline()按行读取'''
# file = open("python12.txt", encoding='utf-8')
# res=file.readline()
# print("1读取的结果是：{}".format(res)) #读取的是第一行

'''readline()按行读取'''
# file = open("python12.txt", encoding='utf-8')
# file.readline()
# res=file.readline()
# print("1读取的结果是：{}".format(res))   #读取的是第二行

'''readlines()全部读取'''
# file = open("python12.txt", encoding='utf-8')
# res=file.readlines()
# print("1读取的结果是：{}".format(res))  #读取后 返回的是一个列表

# file = open("python12.txt",mode="w", encoding='utf-8')
# file.write("C组非常优秀")

# file = open("python13.txt",mode="w", encoding='utf-8')
# file.write("C组非常优秀")

# file = open("python13.txt",mode="a", encoding='utf-8')
# file.write("D组非常OK!")

# file = open("4.txt",mode="a", encoding='utf-8')
# file.write("D组非常OK!")


# file = open("4.txt",mode="w+", encoding='utf-8')
# print(file.read())
# file.write("大喜线儿")

#w+模式
file = open("4.txt",mode="w+", encoding='utf-8')
file.write("study")
print(file.tell())#获取你当前的光标位置



