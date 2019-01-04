#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/11/10 21:43
'''字符串是 Python 中最常用的数据类型。我们可以使用引号("或")来创建字符串。'''

'''Python 不支持单字符类型，单字符在 Python 中也是作为一个字符串使用。
Python 访问子字符串，可以使用方括号来截取字符串，如下实例：'''
# var1 = 'Hello World!'
# var2 = "Runoob"
# print("var1[0]: ", var1[0])
# print("var2[1:5]: ", var2[1:5])

'''你可以截取字符串的一部分并与其他字段拼接，如下实例：'''
# var1 = 'Hello World!'
# print("已更新字符串 : ", var1[:6] + 'Runoob!')


'''在需要在字符中使用特殊字符时，python用反斜杠(\)转义字符。如下表：'''
'''\(在行尾时)	续行符
\\	反斜杠符号
\'	单引号
\"	双引号
\a	响铃
\b	退格(Backspace)
\n	换行'''

#下表实例变量a值为字符串 "Hello"，b变量值为 "Python"：
'''  +	字符串连接	                                                                a + b 输出结果： HelloPython
     *	重复输出字符串	                                                            a*2 输出结果：HelloHello
    []	通过索引获取字符串中字符	                                                a[1] 输出结果 e
 [ : ]	截取字符串中的一部分，遵循左闭右开原则，str[0,2] 是不包含第 3 个字符的。	a[1:4] 输出结果 ell
   in	成员运算符 - 如果字符串中包含给定的字符返回 True	                         'H' in a 输出结果 True
  not in	成员运算符 - 如果字符串中不包含给定的字符返回 True	                     'M' not in a 输出结果 True

 r/R	原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，
 没有转义特殊或不能打印的字符。 原始字符串除在字符串的第一个引号前加上字母 r（可以大小写）以外，
 与普通字符串有着几乎完全相同的语法。
                                                                                        print( r'\n' )
                                                                                        print( R'\n' )'''

# a = "Hello"
# b = "Python"
# print("a + b 输出结果：", a + b)
# print("a * 2 输出结果：", a * 2)
# print("a[1] 输出结果：", a[1])
# print("a[1:4] 输出结果：", a[1:4])
# if ("H" in a):
#     print("H 在变量 a 中")
# else:
#     print("H 不在变量 a 中")
# if ("M" not in a):
#     print("M 不在变量 a 中")
# else:
#     print("M 在变量 a 中")
# print(r'\n')
# print(R'\n')


'''Python字符串格式化
Python 支持格式化字符串的输出 。尽管这样可能会用到非常复杂的表达式，
但最基本的用法是将一个值插入到一个有字符串格式符 %s 的字符串中。'''
# print ("我叫 %s 今年 %d 岁!" % ('小明', 10))
# print ("我叫 %s 今年 %s岁!" % ('小明', 10))

'''Python2.6 开始，新增了一种格式化字符串的函数 str.format()，
它增强了字符串格式化的功能。
基本语法是通过 {} 和 : 来代替以前的 % 。
format 函数可以接受不限个参数，位置可以不按顺序。'''
# a="{} {}".format("hello", "world")    # 不设置指定位置，按默认顺序
# print(a)
# b="{0} {1}".format("hello", "world")  # 设置指定位置
# print(b)
# c="{1} {0} {1}".format("hello", "world")  # 设置指定位置
# print(c)

# print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))
# # 通过字典设置参数
# site = {"name": "菜鸟教程", "url": "www.runoob.com"}
# print("网站名：{name}, 地址 {url}".format(**site))
# # 通过列表索引设置参数
# my_list = ['菜鸟教程', 'www.runoob.com']
# print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的

'''也可以向 str.format() 传入对象：'''
# class AssignValue(object):
#     def __init__(self, value):
#         self.value = value
# my_value = AssignValue(6)
# print('value 为: {0.value}'.format(my_value))  # "0" 是可选的

'''此外我们可以使用大括号 {} 来转义大括号，如下实例：'''
# print ("{} 对应的位置是 {{0}}".format("runoob"))

'''python三引号允许一个字符串跨多行，
字符串中可以包含换行符、制表符以及其他特殊字符。实例如下'''
para_str = """这是一个多行字符串的实例
# 多行字符串可以使用制表符
# TAB ( \t )。
# 也可以使用换行符 [ \n ]。
# """
# print (para_str)

'''在Python3中，所有的字符串都是Unicode字符串。'''
'''Python capitalize()将字符串的第一个字母变成大写,其他字母变小写。
capitalize()方法语法:str.capitalize()
需要注意的是：
1、首字符会转换成大写，其余字符会转换成小写。
2、首字符如果是非字母，首字母不会转换成大写，会转换成小写。'''

# str = "this is string example from runoob....wow!!!"
# print ("str.capitalize() : ", str.capitalize())
#
# str="hello PYTHON"
# print(str.capitalize())
#
# str="123 hello PYTHON"
# print(str.capitalize())
#
# str="@ Hello PYTHON"
# print(str.capitalize())

'''isupper() 方法检测字符串中所有的字母是否都为大写。
isupper()方法语法：str.isupper()
返回值
如果字符串中包含至少一个区分大小写的字符，
并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False'''

# str = "THIS IS STRING EXAMPLE....WOW!!!"
# print (str.isupper())
# str = "THIS is string example....wow!!!"
# print (str.isupper())

'''Python isspace() 方法检测字符串是否只由空白字符组成。
isspace()方法语法：str.isspace()
返回值      如果字符串中只包含空格，则返回 True，否则返回 False.'''
# str = "       "
# print (str.isspace())
# str = "Runoob example....wow!!!"
# print (str.isspace())


'''空白符包含：空格、制表符(\t)、换行(\n)、回车等(\r）
空串不算空白符:'''
# # \t\r\n 都是空白符
# print (' \t\r\n'.isspace()) # True
# print ('\0'.isspace()) # False
# print (' a '.isspace()) # False
# print("".isspace())     #False

'''Python len() 方法返回对象（字符、列表、元组等）长度或项目个数。
len()方法语法：len( s )'''
# str = "runoob"
# # len(str)    # 字符串长度
# print(len(str))
#
# L = [1,2,3,4,5]
# # len(L)          # 列表元素个数
# print(len(L))

'''Python upper() 方法将字符串中的小写字母转为大写字母。
upper()方法语法：str.upper()'''
# str = "this is string example from runoob....wow!!!";
# print ("str.upper() : ", str.upper())


'''Python lower() 方法转换字符串中所有大写字符为小写。
lower()方法语法：str.lower()
返回值    返回将字符串中所有大写字符转换为小写后生成的字符串'''
# str = "Runoob EXAMPLE....WOW!!!"
# print( str.lower() )


'''count() 方法用于统计字符串里某个字符出现的次数。
可选参数为在字符串搜索的开始与结束位置。
count()方法语法：str.count(sub, start= 0,end=len(string))
sub -- 搜索的子字符串
start -- 字符串开始搜索的位置。默认为第一个字符,第一个字符索引值为0。
end -- 字符串中结束搜索的位置。字符中第一个字符的索引为 0。默认为字符串的最后一个位置。'''
# str="www.runoob.com"
# sub='o'
# print ("str.count('o') : ", str.count(sub))
#
# sub='run'
# print ("str.count('run', 0, 10) : ", str.count(sub,0,10))

'''isalnum() 方法检测字符串是否由字母和数字组成。
isalnum()方法语法：str.isalnum()
返回值    如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False'''
# str = "runoob2016"  # 字符串没有空格
# print(str.isalnum())
#
# str = "www.runoob.com"
# print(str.isalnum())

'''Python isalpha() 方法检测字符串是否只由字母组成。
isalpha()方法语法：str.isalpha()
返回值   如果字符串至少有一个字符并且所有字符都是字母则返回 True,否则返回 False'''
# str = "runoob"
# print (str.isalpha())
#
# str = "Runoob example....wow!!!"
# print (str.isalpha())

'''Python isdigit() 方法检测字符串是否只由数字组成。
isdigit()方法语法：str.isdigit()
返回值   如果字符串只包含数字则返回 True 否则返回 False。'''
# str = "123456";
# print (str.isdigit())
#
# str = "Runoob example....wow!!!"
# print (str.isdigit())


'''isnumeric() 方法检测字符串是否只由数字组成。
这种方法是只针对unicode对象。
注：定义一个字符串为Unicode，只需要在字符串前添加 'u' 前缀即可
isnumeric()方法语法：str.isnumeric()
返回值   如果字符串中只包含数字字符，则返回 True，否则返回 False'''
# str = "runoob2016"
# print (str.isnumeric())
#
# str = "23443434"
# print (str.isnumeric())


'''Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。'''
# s1 = "-"
# s2 = ""
# seq = ("r", "u", "n", "o", "o", "b") # 字符串序列
# print (s1.join( seq ))
# print (s2.join( seq ))


# jn1="-"
# jn2="------"
# str='name'
# print(jn1.join(str)) #n-a-m-e   #字符串也属于序列
#
# print(jn2.join(str) )   #'n------a------m------e'#使用多字符连接序列
#
# fruits={'apple','banana'}
# print(jn1.join(fruits))   #'apple-banana'#连接的序列是集合
#
# animals=("pig","dog")
# print(jn1.join(animals))   #'pig-dog'#连接的序列是元祖
#
# students={"name1":"joy","name2":"john","name3":"jerry"}   #连接的序列是字典，会将所有key连接起来
# print(jn1.join(students))     #'name1-name2-name3''


'''lstrip() 方法用于截掉字符串左边的空格或指定字符。'''
# str = "     this is string example....wow!!!     "
# print( str.lstrip() )
# str = "88888888this is string example....wow!!!8888888"
# print( str.lstrip('8') )


'''swapcase() 方法用于对字符串的大小写字母进行转换。'''
# str = "this is string example....wow!!!"
# print (str.swapcase())
#
# str = "This Is String Example....WOW!!!"
# print (str.swapcase())


'''max() 方法返回字符串中最大的字母。在有大小写的字符串中返回的是小写字母的最大值'''
# str = "runoob"
# print ("最大字符: " ,max(str))
# str = "rUnoob"
# print ("最大字符: " ,max(str))