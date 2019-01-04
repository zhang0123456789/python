#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/11/5 20:47

#有一个字典：
# {"广东":["深圳","广州","阳江"],
# "湖南":["长沙","益阳","怀化"],
# "湖北":["武汉","襄阳","黄冈"]}
#你从控制台输入一个省份
#根据你的省份判断 你可以选择哪些城市
# 当你选择完毕后，就打印一个信息到控制台，告诉你，
# 你选择了XX省份XX城市 #如果省份不存在 或者是城市不存在
# 那么就告诉你 你输入错误 终止程序
# d={"广东":["深圳","广州","阳江"],
# "湖南":["长沙","益阳","怀化"],
# "湖北":["武汉","襄阳","黄冈"]}
# province=input("请输入您的省份：")
# if province in d.keys():
#     city=input("请输入您的城市：")
#     if city in d[province]:
#             print("你选择的{}省{}城市".format(province,city))
#     else:
#         print("你输入的城市不存在")
# else:
#     print("你输入的省份不存在")


#循环的意思是：重复的做每件事情
#执行循环：触发条件
#终止循环：终止条件  如果没有的话  就不能停止  死循环


#while条件表达式：#比较运算、逻辑运算、成员运算、数据非空和空的情况，你要循环的代码/执行的语句
#用法：while后面的条件成立（true）那么就执行，不成立就（false）就不执行
#重点：每次执行完毕后，就会重新判断while后面的条件，在觉得是否循环

#死循环
# while 1:
#     print("我现在是一个while循环")  #死循环
'''破解死循环---设置终止条件
#1）while与break的结合使用  break:终止循环、退出循环
#2）加一个终止条件  加一个变量控制次数---推荐使用'''

''' 只执行一次
# while 1:
#     print("我现在是一个while循环")
#     break #  只执行一次'''

# count=1 #次数的初始值
# while 1:
#     print("我现在是一个while循环")
#     count+=1#每次代码执行代码后  +1
#     if count==10:
#         break  #执行9次

# count=1 #次数的初始值
# while 1:
#     print("我现在是一个while循环")
#     count+=1#每次代码执行代码后
#     if count==11:
#         break  #执行10次

# count=1#次数的初始值
# a=10
# while a>0:
#     print("我现在是一个while循环")
#     count+=1
#     if count==10:#每次执行代码后
#         break

# count = 1  # 次数的初始值
# a = 10
# while 10 > 0:
#     print("我现在是一个while循环")
#     count += 1
#     if count == 10:  # 每次执行代码后
#         break

'''技巧：尽量不要让while后面一直是true'''

# count = 1  # 次数的初始值
# a = 10
# while True:
#         print("我现在是一个while循环")
#         count += 1
#         if count == 10:  # 每次执行代码后
#             break

# if 1:
#     print("我是if后面的代码")

#破解死循环——设置终止条件
#1）while与break的结合使用  break:终止循环/退出循环
#2）加一个终止条件
#利用while循环求1-100的和
# a=1
# total=0
# while a<101:
#     total+=a
#     a+=1
# print(total)  #打印5050

# count=1
# sum=0
# while count<101:
#     sum+=count
#     count+=1
# print("打印1-100的和：{}".format(sum))

#缩进位置不同，打印出的结果会不一样
# count=1
# sum=0
# while count<101:
#     sum+=count
#     count+=1
#     print("打印每次相加的和：{}".format(sum))

# a=1
# total=0
# while true:
#     total+=a
#     a+=1
#     if a>100:
#         break
# print(total)

'''for 循环  遍历元素
#遍历 ：访问这个数据里面的么一个元素  按顺序挨个访问'''
# s='David_zhang'
'''语法：for item in 数据/指定的数据范围:
               代码块'''

# for item in 'Dacid_zhang':
#     print(item)

# s='Dacid_zhang'
# for item in s:
#     print(item)

'''end用来不换行输出'''
# s='Dacid_zhang'
# for item in s:
#     print(item ,end=' ')

'''格式为  for_in_:'''
# s='Dacid_zhang'
# for domino in s:
#     print(domino ,end=' ')

# s=(1,0.02,'elf',('wendy','蓝色火'))
# for item in s:
#     print(item)

# s=(1,0.02,'elf',('wendy','蓝色火'))
# for item in s:
#     print(item,end=',')

# s=([1,2],[3,4],[5,6],[7,8],"0.02")
# for item in s:
#     print(item)

# s=([1,2],[3,4],[5,6],[7,8],"0.02")
# for item in s:
#     print(item,end=',')

'''默认访问的是key'''
# s={"name":"小麦","adress":"杭州"}
# for item in s:
#     print(item)


'''打印key'''
# s={"name":"小麦","adress":"杭州"}
# for item in s.keys():
#     print(item)

'''打印value'''
# s={"name":"小麦","adress":"杭州"}
# for item in s.values():
#     print(item)

# s={"name":"小麦","adress":"杭州"}
# for item in s:
#   print(s[item])

# s={"name":"小麦","adress":"杭州"}
# for item in s.keys():
#   print(s[item])

'''同时打印key  value'''
# s={"name":"小麦","adress":"杭州"}
# for key,value in s.items():
#     print(key,value)

# s={"name":"小麦","adress":"杭州"}
# for a,b in s.items():
#     print(a,b)

'''range函数  生成一个指定范围的整数序列
range(m,n,k) m=开头  n=到哪个数结尾 k=步长 取头不取尾'''
# s=list(range(1,5,2))
# print(s)  #打印[1,3]

# s=list(range(1,5))
# print(s)  #打印[1,2,3,4]

# s=list(range(5))
# print(s)  #打印[0,1,2,3,4]


'''利用for循环完成1-100的循环'''
# total=0
# for i in range(1,101):
#     total+=i
# print(total)#打印5050

# total=0
# for i in range(1,101):
#     total+=i
# print("1-100的和:{}".format(total))   #打印5050

# total=0
# for i in range(1,101):
#     total+=i
#     print(total)#每执行一次打印total

'''for 循环永远不会进入死循环
for循环的次数  是遍历的数据里面元素的个数决定'''

# s={"name":"小麦","adress":"杭州"}
# for i in s:
#     print ("我是代码块")   #打印俩个 我是代码块


'''利用for循环把每个名 分别打印出来'''
# L = [['Apple','Goole','Microsoft','sfsf'],
#      ['Java','Python','Ruby','PHP'],
#      ['Adam','Bart','Lisa',"adaf"]]
# for item in L:
#     print(item)
#     for value in item:
#         print(value)


#1*1   i=1 j=1
#1*2=2 2*2=4 i=2 j(1,3)
#1*3=3 2*3=6 3*3=9 i=3 j(1,4)
#1*4=4 2*4=8 3*4=12 4*4=16  i=4 j(1,5)


# for i in range(1,10):
#     for j in range(1,i+1):
#         print("{}*{}={}" .format(i,j,i*j), end="  ")
#     print()


# list_1=[[1,2,3,4],[5,6,7,8]]
# for i in range(len(list_1)):
#     for j in range(len(list_1[i])):
#         print(list_1[i][j])


'''进入死循环'''
# number=23
# while True:
#     guess=int(input("请输入一个整数："))
#     if guess==number:
#         print("恭喜你猜对啦")
#     elif guess<number:
#         print("你输入的数字太小了")
#     else:
#         print("你输入的数字太大了")


'''break  continue  结合使用'''
'''break常用于循环结构，出现break的时候，能将该循环强制停止，然后退出循环
continue功能是强制停止循环中的这一次执行，直接跳到下一次执行'''
# number=23
# while True:
#     guess=int(input("请输入一个整数："))
#     if guess==number:
#         print("恭喜你猜对啦")
#         break
#     elif guess<number:
#         print("你输入的数字太小了")
#         continue
#     else:
#         print("你输入的数字太大了")
#         continue

number=23
count=10
while True:
    guess=int(input("请输入一个整数："))
    if guess==number:
        print("恭喜你猜对啦")

    elif guess<number:
        print("你输入的数字太小了")

    else:
        print("你输入的数字太大了")
    count-=1