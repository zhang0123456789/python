#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/11/15 6:53
'''.实现用户输入用户名和密码，当用户名为 seven或alex且 密码为123时，
显示登陆成功，否则登陆失败，失败时允许重复输入三次'''
# count=0
# while 1:
#     name_1=input("请输入用户名：")
#     pwd=input("请输入密码：")
#     if name_1=='seven'or name_1=='alex'and pwd==123:
#         print("登录成功")
#         break
#     else:
#         print("登录失败")
#         count += 1
#         if count==3:
#             exit()
#
# count=3
# while count>0:
#     name=input("请输入用户名")
#     pwd=input("请输入密码")
#     if name =='seven' or name =='alex'and pwd=='123' :
#         print("登录成功")
#         break
#     else:
#         print("密码错误，请重新输入")
# else:
#     print("登录失败")
# count-=1


'''使用while循环实现输出2-3+4-5+6.....+100的和'''
# sum_1=0
# sum_2=0
# for i in range(2,101,2):
#     sum_1+=i
# print(sum_1)
# for j in range(-3,-100,-2):
#     sum_2+=j
# print(sum_2)
# print(sum_1+sum_2)
#
# sum=0
# for i in range(2,101):
#     if i%2==0:
#         sum+=i
#     else:
#         sum-=i
# print(sum)


'''求1-2+3-4+5 ... 99的所有数的和'''
# sum=0
# for i in range(1,100):
#     if i%2==0:
#         sum-=i
#     else:
#         sum+=i
# print(sum)

'''使用while循环输入 1 2 3 4 5 6     8 9 10'''
# i=0
# while i<10:
#     i+=1
#     if i==7:
#         continue
#     else:
#         print(i,end=' ,')

'''输出 1-100 内的所有奇数'''
# for i in range(1,101,2):
#     print(i,end=',')

# for i in range(1,101):
#     if i%2 ==1:
#         print(i,end=',')

# count=1
# while count<100:
#     if count%2==1:
#         print(count,end=',')
#     count+=1

'''输出 1-100 内的所有偶数'''
# for i in range(2,101,2):
#     print(i,end=',')

# for i in range(1,101):
#     if i%2==0:
#         print(i,end=',')

# count=1
# while count<101:
#     if count%2==0:
#         print(count,end=',')
#     count+=1

'''分别书写数字5，10,32,7的二进制表示'''
# a=[5,10,32,7]
# for i in a:
#     print(i,":",bin(i))   #二进制
#     print(i,":",oct(i))   #八进制
#     print(i,":",hex(i))   #十六进制

'''求 1-100 内的所有数的和'''
# sum=0
# for i in range(1,101):
#     sum+=i
# print("1-100的和：",sum)

# sum=0
# count=1
# while count<101:
#     sum+=count
#     count+=1
# print("1-100的和：",sum)

# sum=0
# count=1
# while True:
#     sum+=count
#     count+=1
#     if count==101:
#         break
# print("1-100的和：",sum)

'''dic={'k1':"v1","k2":"v2","k3":[11,22,33]}
a. 请循环输出所有的 key
b. 请循环输出所有的 value
c. 请循环输出所有的 key 和 value
d. 请在字典中添加一个键值对， "k4":"v4"，输出添加后的字典
e. 请在修改字典中 "k1" 对应的值为 "alex"，输出修改后的字典
f. 请在 k3 对应的值中追加一个元素 44，输出修改后的字典
g. 请在 k3 对应的值的第 1 个位置插入个元素 18，输出修改后的字典'''
# dic={'k1':"v1","k2":"v2","k3":[11,22,33]}
# for a in dic.keys():
#     print(a,end=",")
#
# for b in dic.values():
#     print(b,end=",")
#
# for c in dic.items():
#     print(c,end=",")
#
# dic['k4']='v4'
# print(dic)
#
# dic['k1']='alex'
# print(dic)
#
# dic['k3'].append(44)
# print(dic)
#
# dic['k3'].insert(0,18)
# print(dic)



'''19、写代码，有如下变量，请按照要求实现每个功能

name = " aleX "
a.移除name变量对应的值两边的空格，并输入移除有的内容
b.判断name变量对应的值是否以 "al"开头，并输出结果
c.判断name变量对应的值是否以 "X"结尾，并输出结果
d.将name变量对应的值中的 " l" 替换为 " p"，并输出结果
e.将name变量对应的值根据 " l" 分割，并输出结果。
f.请问，上一题 e分割之后得到值是什么类型？
g.将name变量对应的值变大写，并输出结果
h.将name变量对应的值变小写，并输出结果
i.请输出name变量对应的值的第2个字符？
j.请输出name变量对应的值的前3个字符？
k.请输出name变量对应的值的后2个字符？
l.请输出name变量对应的值中 "e" 所在索引位置？'''
name = " aleX "
print(name.strip())       #'aleX'

print(name.startswith("al"))      #False

print(name.endswith("X") )        # False

print(name.replace("l","p") )           # ' apeX '

print(name.split('l'))               # [' a', 'eX ']

print(type(name.split('l')) )        # <class 'list'>

print(name.upper()  )         # ' ALEX '

print(name.lower())                   # ' alex '

print(name[1] )             # 'a'

print(name[:2])             # ' a'7

print(name[-2:] )                # 'X '

print(name.index("e") )               # 3
