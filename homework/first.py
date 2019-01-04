#!/usr/bin/env python
#-*- coding:utf-8 -*-
L = [['Apple','Goole','Microsoft'],['Java','Python','Ruby','PHP'],['Adam','Bart','Lisa']]
print(L[0][0])
print(L[1][1])
print(L[2][2])



a=[1,7,4,89,34,2]
# print(len(a))
for i in range(0,len(a)-1):  #循环遍历从0开始到倒数第二个元素下标
    for j in range(0,len(a)-1-i):#循环遍历从0开始，把最大数放末尾
        if a[j]>a[j+1]:      #判断数字大小，小的放前面，大的放后面
            a[j],a[j+1]=a[j+1],a[j]
print(a)


str=input("请输入年月日:");
print(str[0:4]+"年",str[4:6]+"月",str[-1]+"日")







