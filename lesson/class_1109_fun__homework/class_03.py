#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/11/9 20:02
import os

'''1、模块名称不要和第三方库和本地库名字冲突
2、导入模块的时候，  寻找顺序：先到当前目录找
 然后在去我们配置的环境变量里面找'''

'''相对路径:在跟自己同级的目录在找
绝对路径：任何情况下都不会出错的'''
# open("python12.txt")#相对路径
# open("study/python13.txt")#打开一个文件
# open("../python13.txt")#打开一个文件  返回到上一级
# open("E:\python_study\class1109\python12.txt")#copy path

#导入模块
#import  #具体到模块名
#import...as
#from...import  #推荐使用  可以具体到方法名 只是具体到模块名
#from...import...as...
#from...import *
'''自己安装的库 本地库 我们可以直接从包名开始定位
一层一层的去定位、定位'''

import email.mime.text

#测试代码
#if __name__ == '__main__':  #代码执行入口  只有运行当前文件的时候才会运行下面的代码

# from class1109_funtion.class_02 import add  #具体到方法# add(101)
# sub(101)

# from class1109_funtion.import.class_02  #具体到模块名
# class_02.sub(101)

# from class1109_funtion.study.test2.class_02 import *
# add(101)
# sub(101)

# from class1109_funtion.study.test2.class_02 import sub as x
# x(101)    #给方法取别名