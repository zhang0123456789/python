#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/11/25 9:15
import os
#E:\python_study\lesson\class_1112_file&path\class_path.py

'''新建目录    支持相对路径 支持绝对路径  '''
# os.mkdir("Python12")
# os.mkdir('E:\python_study\lesson\class_1112_file&path\Python12')


'''删除一个目录'''
# os.rmdir("Python12")


'''建立多级目录  不可以越级新建目录，除最后一级以外的都存在'''
# os.mkdir("python12/A")

'''建立多级目录，确认前面的目录存在才可以建立成功'''
# os.mkdir("python12")
# os.mkdir("python12/A")

'''删除包含有子文件夹的目录   不可以跨级删除'''
# os.rmdir("python12/A")

'''os.getcwd()获取当前的工作路劲  具体到目录  不具体到文件'''
# path=os.getcwd()  #不需要传参
# print(path)

'''realpath()获取当前的工作路劲  具体到文件  如果参数是：_file_就说明是所在的绝对路径'''
# path_2=os.path.realpath(__file__)    #__file__表示文件本身
# print(path_2)


'''方法一  绝对路径'''
'''方法二  相对路径'''
'''方法三、如果获取python12文件夹下面子文件夹A下的b.txt'''
# cwd_path=os.getcwd()
# txt_path=cwd_path+"/python12/A/b.txt"
# print(txt_path)

'''方法四、realpath'''
# real_path=os.path.realpath(__file__)
# print(real_path)
# print(os.path.split(real_path))  #split返回的是元组
# print(os.path.split(real_path)[0]+"/python12/A/b.txt")


'''os.path.split(路径)  拆分路径  这样可以把一个路径拆分为俩部分
后一部分总是最后级别的目录或文件名  返回元组'''
# real_path=os.path.realpath(__file__)
# print(real_path)
# print(os.path.split(real_path))  #split返回的是元组
# print(os.path.split(os.path.split(real_path)[0]))
# print(os.path.split(real_path)[0]+"/python12/A/b.txt")



'''os.path.isdir:判断当前文件是否是目录 返回布尔值
os.path.isfile:判断当前文件是否是文件，返回布尔值'''
real_path = os.path.realpath(__file__)
print(real_path)
print(os.path.isdir(real_path))   #返回false
print(os.path.isfile(real_path))   #返回True
print(os.listdir(os.path.split(real_path)[0]))  #传入一个目录的路径
print(os.path.dirname(real_path))   #返回目录
print(os.path.basename(__file__)) #返回当前文件名     返回class_path.py



'''拼接路径的函数  os.path.join'''
path=os.getcwd()
new_path=os.path.join(path,"python13")
print(new_path)


# path=os.getcwd()
# new_path=os.path.join(path,"python13",'B')
# print(new_path)

'''中间可以用，分开 可以拼接多级目录'''
# path=os.getcwd()
# new_path=os.path.join(path,"python13",'B','1')
# print(new_path)

'''中间可以用/分开  可以拼接多级目录'''
# path=os.getcwd()
# new_path=os.path.join(path,'python13\B\one')
# print(new_path)

'''不能以数字开头，所有打印不出来1的目录'''
# path=os.getcwd()
# new_path=os.path.join(path,'python13\B\1')
# print(new_path)