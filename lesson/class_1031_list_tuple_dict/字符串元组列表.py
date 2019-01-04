#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/11/2 20:59
#字符串内建函数
#find()函数：返回-1表示未找到字符串，如果找到了就返回对应的索引
#format(）函数：格式化字符串
#isdigit()函数：如果只包含数字，就返回true 否则返回false
#replace()函数：指定替换内容以及被替换内容字符串，并且可以指定替换次数
#split()函数：根据指定字符对字符串进行切割
#strip()函数：去掉头和尾指定的字符
#upper()函数：字符串字母转换成大写
#lower（）函数：字符串的字母转换成小写

#字符串
# s=''#空字符串

#1：字符串的拼接
# s_1="我的名字是："
# s_2='sai'
# s_3=s_1+s_2
# print(s_3)#print("拼接后的字符串是:",s_3)

# s_1="我的名字是："
# s_4=5
# s_3=s_1+s_4#TypeError: can only concatenate str (not "int") to str
# print(s_3) #字符串和整数不能直接拼接

#如果说数字和字符串拼接，那么可以把数字强制转字符串
# s_1="我的名字是："
# s_4=5
# s_3=s_1+str(s_4)
# print(s_3)
# print("拼接后的字符串是：",s_3)#函数的不同参数


# s_1="我的名字是："
# s_4=5
# s_3=s_1+str(s_4)
# print(s_3)
# print("拼接后的字符串是：",s_3,s_1,s_4)#函数与参数之间用逗号隔开
# a=1
# b=2
# c=3
# print(a,b,c)

#字符串的格式化输出
# name="wendy"
# course="python"
# class_id=12
# age=23
# salary=150000
# print('''=======wendy's info=======''')
# print("姓名是：",name)
# print("班级是:",course)
# print("年龄是:",age)
# print("期望薪资:",salary)

#% 占位符  占坑符
#%s  string表示这里占了一个坑 要放字符串进来哟
#%d  digital表示这里占了一个坑 要放整数进来

# name="wendy"
# course="python"
# class_id=12
# age=23
# salary=150000
# print('''======wendy's info=====
# 姓名是:%s
# 班级是:%s,%d
# 年龄是:%d
# 期望薪资:%d'''%(name,course,class_id,age,salary))


# name="wendy"
# course="python"
# class_id=12
# age=23
# salary=150000
# print('''======wendy's info=====
# 姓名是:%s
# 班级是:%s,%d
# 年龄是:%d
# 期望薪资:%d'''%(name,course,class_id,age,age))

# name="wendy"
# course="python"
# class_id=12
# age=23
# salary=150000
# print('''======wendy's info=====
# 姓名是:%s
# 班级是:%s%d
# 年龄是:%d
# 期望薪资:%d'''%(name,course,class_id,age,salary))

# name="wendy"
# course="python"
# class_id=12
# age=23
# salary=150000
# print('''======wendy's info=====
# 姓名是:%s
# 班级是:%s====%d
# 年龄是:%d
# 期望薪资:%d'''%(name,course,class_id,age,salary))

# name="wendy"
# course="python"
# class_id=12
# age=23
# salary=150000
# print('''@@@@@@wendy's info@@@@@
# 姓名是:%s
# 班级是:%s,%d
# 年龄是:%d
# 期望薪资:%d'''%(name,course,class_id,age,salary))

#根据你的%s%d去分配值，按顺序赋值一一对应
# name="wendy"
# course="python"
# class_id=12
# age=23
# salary=150000
# print('''@@@@@@***wendy's info@@@@@***
# 姓名是:%s
# 班级是:%s蜜蜜蜜蜜%d
# 年龄是:%d
# 期望薪资:%d'''%(name,course,class_id,age,salary))


#%d只能放数据，%s可以放数据、字符串、任何数据
# name="wendy"
# course="python"
# class_id=12
# age=23
# salary=150000
# print('''@@@@@@***wendy's info@@@@@***
# 姓名是:%s
# 班级是:%s,%s
# 年龄是:%s
# 期望薪资:%s'''%(name,course,class_id,age,salary))

# name="wendy"
# course="python"
# class_id=12
# age=23
# salary=150000
# print('''@@@@@@***wendy's info@@@@@***
# 姓名是:%s
# 班级是:%s,%s
# 年龄是:%f
# 期望薪资:%f'''%(name,course,class_id,age,salary))


#格式化输出2   .format{}
# name="wendy"
# course="python"
# class_id=12
# age=23
# salary=150000
# print('''@@@@@@***wendy's info@@@@@***
# 姓名是:{}
# 班级是:{},{}
# 年龄是:{}
# 期望薪资:{}'''.format(name,course,class_id,age,salary))#按顺序根据{}赋值

# name="wendy"
# course="python"
# class_id=12
# age=23
# salary=150000
# print('''@@@@@@***wendy's info@@@@@***
# 姓名是:{1}
# 班级是:{1},{1}
# 年龄是:{1}
# 期望薪资:{1}'''.format(name,course,class_id,age,salary))#{}里面 可以指定顺序 按照你指定顺序去赋值


# name="wendy"
# course="python"
# class_id=12
# age=23
# salary=150000
# print('''@@@@@@***wendy's info@@@@@***
# 姓名是:{0}
# 班级是:{1},{2}
# 年龄是:{3}
# 期望薪资:{4}'''.format(name,course,class_id,age,salary))

#指定顺序的时候要么都指定要么都不指定
# name="wendy"
# course="python"
# class_id=12
# age=23
# salary=150000
# print('''@@@@@@***wendy's info@@@@@***
# 姓名是:{0}
# 班级是:{1},{2}
# 年龄是:{3}
# 期望薪资:{8}'''.format(name,course,class_id,age,salary))#  指定顺序超过长度，不能运行成功

# print("我是{},我今年{}".format(12,"orange"))
# print("我是{0},我今年{0}".format(12,"orange"))
#print("我是{1},我今年{1}".format(12,"orange"))


#字符串的内建函数   神奇的用法
s='明天，你好！'
# #查找某个字符串  字符串.find(你指定的字符或子字符串)
print(s.find("@"))#-1  返回-1，如果没有找到就返回-1
print(s.find("好"))#4  返回4，如果找到了就返回索引号
# print(s.find("你好"))#3  返回3，如果传入的是子字符串，如果找到了就返回第一个字符串的索引位置值

#字符串的替换  字符串.replace(目标，最终替换成什么)
# s='舞飞扬'
# new_s=s.replace("飞","叶子")#替换后的字符串  存起来
# print(new_s)

#1、单词容易写错
#2、替换之后未保存，输出的还是原来的字符串
# s='舞飞扬'
# new_s=s.repalce("飞","叶子")#AttributeError: 'str' object has no attribute 'repalce'  单词容易写错
# print(new_s)

# s='舞飞扬'
# new_s=s.replace(s[1],"叶子")#替换后的字符串  存起来
# print(new_s)

#切割  字符串.split()#返回的数据类型  是列表  列表里面的元素都是字符串类型
# s='hi@你好'
# value=s.split('@')
# print("split切割后的结果值{}".format(value))#切割之后是俩个字符串

# s='hi@你@好'
# value=s.split('@')
# print("split切割后的结果值{}".format(value))#切割之后是3个字符串


# s='hi@你@好@'
# value=s.split('@')
# print("split切割后的结果值{}".format(value))#切割之后是4个字符串
# print(len(value))


# s='hi@你@好@@'
# value=s.split('@')
# print("split切割后的结果值{}".format(value))#切割之后是5个元素
# print(len(value))



# s='hi@你@好@@'
# value=s.split('@',1)
# print("split切割后的结果值{}".format(value))#切割之后是2个元素

# s='hi@你@好@@'
# value=s.split('@',2)
# print("split切割后的结果值{}".format(value))#切割之后是3个字符串

#去除指定字符串
# s='666我就是喜欢python66666666'
# print(s.strip('6'))


#字符串.strip()  去掉头尾指定的字符
# s='666我就是喜欢6666666666666python66666666'
# print(s.strip('6'))


# s='      666666我就是喜欢6666666666666python66666666'
# print(s)
# print(s.strip(' '))#去掉空格

#变换大小写  字符串.upper()都变大写
#变换大小写  字符串.lower()都变小写
# str_1='hello'
# print(str_1.upper())


# str_1='hello'
# print(str_1.upper().lower())

# str_2='HHHUUU'
# print(str_2.lower())

# str_3='hElo'
# print(str_3.upper())
# print(str_3.capitalize())#首字母大写
# print(str_3.index('E'))#找字符所在的索引
# print(str_3.swapcase())#大小写互换
# print(str_3.isdigit())#判断输入的字符串是否是数字 如果是纯数字 返回True  否则是false

'''元组的关键字  tuple()'''
# t=(1)
# print(type(t))#  type类型

'''
#1、可以有空元组
#2、如果只有一个数据 请加一个逗号，不然会变成一个非元组的数字
#3、元素之间用逗号隔开
# t=(1,)
# print(type(t))#  type类型'''

#3、什么类型的数据都可以放
# t=(1,0.02,'hello',(1,'666','python'))

#4、取单个元素  元组名[索引值]
#5、支持切片 同字符串操作
# t=(1,0.02,'hello',(1,'666','python'))
# print(t[-1])
# print(t[3])
# print (t[0:3:2])#取(1, 'hello')

#6、嵌套 元组里面还有子元组
# t=(1,0.02,'hello',(1,'666','python'))
# print(t[-1][1])#取值666
# print(t[-1][2])#取值python

'''7、唯一一个忌讳点    元组里面的值不能修改
#8、tuple()有序不可变'''
# t=(1,0.02,'hello',(1,'666','python'))
# t[0]='sum'#TypeError: 'tuple' object does not support item assignment 不能修改


# t=(1,0.02,'hello',(1,'666','python'))
# print(t.count('hello'))# 统计hello的个数
# print(t.index('hello'))#查找hello的索引值

'''元组里面的值不能修改 增删改  全部禁止'''
t_2=(1,2,0.02,'sunflower',('sunny',33,'薄荷糖'),[6,7,8,9,'柠檬班'])
t_2[-1][-1]='ch'
print(t_2)

'''元组不能整体替换，即不能改整个列表，可以改列表里面的单个元素'''
# t_2=(1,2,0.02,'sunflower',('sunny',33,'薄荷糖'),[6,7,8,9,'柠檬班'])
# t_2[-1]='ch'
# print(t_2)#不能成功运行


#列表  list[]
# L=[1,2,0.02,'sunflower',('sunny',33,'薄荷糖'),[6,7,8,9,'柠檬班']]
'''1、空列表
#2、元素之间用逗号隔开
#3、什么类型的数据都可以放'''
# print(L[3])#取值sunflower
# print(L[-2])#取值('sunny', 33, '薄荷糖')
# print(L[1:4:2])#取值[2, 'sunflower']
#4、嵌套 元组 列表
# print(L[4][-1])#取值薄荷糖

#列表 增删改查 样样都行 列表里面的元组可以整体替换但元组里面的部分不能替换

'''函数添加   list.append()加入列表最后'''
# L=[1, 2, 0.02, 'sunflower', ('sunny', 33, '薄荷糖'), [6, 7, 8, 9, '柠檬班']]
# L.append("精灵1")#每次只能添加一个数据  只能放最后
# print(L)
'''列表的添加  加入指定位置   list.insert()'''
L=[1, 2, 0.02, 'sunflower', ('sunny', 33, '薄荷糖'), [6, 7, 8, 9, '柠檬班']]
L.insert(0,'寒风')
print(L)

'''删除
#L.pop()默认删除最后一个元素'''
#L.pop(i)根据你指定的索引 删除指定的元素
# L=[1, 2, 0.02, 'sunflower', ('sunny', 33, '薄荷糖'), [6, 7, 8, 9, '柠檬班']]
# L.pop(1)
# print(L)

'''修改 列表名[索引]=新值'''
L=[1, 2, 0.02, 'sunflower', ('sunny', 33, '薄荷糖'), [6, 7, 8, 9, '柠檬班']]
L[0]='放飞'
print(L)

'''拓展
#从小到大的元素'''
# L=[9,8,7,6,5,4,3,2,1]
# L.sort()#排序 从小到大的元素
# print(L)#输出[1, 2, 3, 4, 5, 6, 7, 8, 9]


'''倒序  本末倒置'''
# L=[9,8,7,6,5,4,3,2,1,'arlene']
# L.reverse()#倒序  本末倒置
# print(L)#输出['arlene', 1, 2, 3, 4, 5, 6, 7, 8, 9]

# L=[9,8,7,6,5,4,3,2,1,'arlene']
# print(L.count(4))

# L=[9,8,7,6,5,4,3,2,1,'arlene']
# print(L.index(1))

''' extend  把俩个列表放在一块 一次性 可以加多个元素'''
# L=[9,8,7,6,5,4,3,2,1,'arlene']
# S=[404,'棋幻人生']
# L.extend(S)#把俩个列表放在一块 一次性 可以加多个元素
# print(L)

'''remove  根据指定的元素删除，只会删除一个'''
# L=[9,8,7,6,5,4,3,2,1,'arlene',9 ,9]
# L.remove(9)
# print (L)