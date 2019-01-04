#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/11/25 21:38
# for m in range(1,5):
#     for n in range(1,5):
#         print(m," ",n)
#     print(" ")

# for m in range(1,5):
#     for n in range(1,m+1):
#         print(m," ",n)
#     print(" ")

# for m in range(1,5):
#     for n in range(1,m+1):
#         print(n," ",m)
#     print("")

# for m in range(1,5):
#     for n in range(1,m+1):
#         print(n, m,end='    ')
#     print("  ")

'''九九乘法表'''
# for m in range(1,10):
#     for n in range(1,m+1):
#         print("{}*{}={}".format(n,m,n*m),end='  ')
#     print(" ")

'''水仙花数:题目：打印出所有的“水仙花数”，所谓“水仙花数”是指一个三位数，其各位数字立方和等于该数 
   本身。例如：153是一个“水仙花数”，因为153=1的三次方＋5的三次方＋3的三次方
'''
# for m in range(100,999):
#     i=m//100
#     j=m//10%10
#     k=m%10
#     if i*100+j*10==i**3+j**3+k**3:
#         print(m)

'''写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，
并将其作为新的列表返回给调用者 '''
def func(p,q):
    result=[]
    for i1 in range(len(p)):
        if i1 % 2 ==1:
            result.append(p[i1])
    for i2 in range(len(q)):
        if i2 % 2 ==1:
            result.append(q[i2])
    print(result)
r=func([11,22,33],(11,22,33))


'''写函数，检查传入字典的每一个value的长度，如果大于2，
那么仅仅保留前两个长度的内容，并将新内容返回给调用者
dic = {“k1”: "v1v1","k2":[11,22,33}}'''


def func1(**p):
    for key, value in p.items():
        if len(value) > 2:
            p[key] = value[0:2]
    return p
r = func1(k1="v1v1", k2=[11, 22, 33, 44, 55])
print(r)






