#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/11/11 11:36
'''字典是另一种可变容器模型，且可存储任意类型对象。
字典的每个键值(key=>value)对用冒号(:)分割，
每个对之间用逗号(,)分割，整个字典包括在花括号({})中 ,格式如下所示：
d = {key1 : value1, key2 : value2 }'''

'''键必须是唯一的，但值则不必。值可以取任何数据类型，
但键必须是不可变的，如字符串，数字或元组。
dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}'''

'''访问字典里的值   把相应的键放入到方括号中，如下实例:'''
# dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# print("dict['Name']: ", dict['Name'])
# print("dict['Age']: ", dict['Age'])

'''修改字典   向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对如下实例:'''
# dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# dict['Age'] = 8;  # 更新 Age
# dict['School'] = "菜鸟教程"  # 添加信息
# print("dict['Age']: ", dict['Age'])
# print("dict['School']: ", dict['School'])


'''删除字典元素
能删单一的元素也能清空字典，清空只需一项操作。
显示删除一个字典用del命令，如下实例：'''
# dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# del dict['Name']  # 删除键 'Name'
# dict.clear()  # 清空字典
# del dict  # 删除字典
# print("dict['Age']: ", dict['Age'])
# print("dict['School']: ", dict['School'])

'''不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住，如下实例：'''
# dict = {'Name': 'Runoob', 'Age': 7, 'Name': '小菜鸟'}
# print("dict['Name']: ", dict['Name'])

'''键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行，如下实例：'''

'''	len(dict)   计算字典元素个数，即键的总数。'''
# dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# print(len(dict))

'''str(dict)   输出字典，以可打印的字符串表示。'''
# dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# print(str(dict))
# print(type(str(dict)))

'''Python 字典 in 操作符用于判断键是否存在于字典中，如果键在字典 dict 里返回 true，否则返回 false。
而 not in 操作符刚好相反，如果键在字典 dict 里返回 false，否则返回 true。
in 操作符语法：  key in dict'''
# dict = {'Name': 'Runoob', 'Age': 7}
# # 检测键 Age 是否存在
# if 'Age' in dict:
#     print("键 Age 存在")
# else:
#     print("键 Age 不存在")
#
# # 检测键 Sex 是否存在
# if 'Sex' in dict:
#     print("键 Sex 存在")
# else:
#     print("键 Sex 不存在")
#
# # not in
# # 检测键 Age 是否存在
# if 'Age' not in dict:
#     print("键 Age 不存在")
# else:
#     print("键 Age 存在")

'''Python 字典 items() 方法以列表返回可遍历的(键, 值) 元组数组。
items()方法语法：  dict.items()'''
# dict = {'Name': 'Runoob', 'Age': 7}
# print ("Value : %s" %  dict.items())

# dict = {'Name': 'Runoob', 'Age': 7}
# for i,j in dict.items():
#     print(i, ":\t", j)
#
# dict = {'Name': 'Runoob', 'Age': 7}
# for i, j in dict.items():
#      print(i, ":", j)


'''将字典的 key 和 value 组成一个新的列表：'''

d={1:"a",2:"b",3:"c"}
result=[]
for k,v in d.items():
    result.append(k)
    result.append(v)

print(result)


'''Python 字典 get() 函数返回指定键的值，如果值不在字典中返回默认值。
get()方法语法：  dict.get(key, default=None)'''

'''以下实例展示了 get()函数的使用方法：'''
# dict = {'Name': 'Runoob', 'Age': 27}
# print ("Age 值为 : %s" %  dict.get('Age'))
# print ("Sex 值为 : %s" %  dict.get('Sex', "NA"))

'''Python 字典 copy() 函数返回一个字典的浅复制。
copy()方法语法：  dict.copy()'''
# dict1 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# dict2 = dict1.copy()
# print("新复制的字典为 : ", dict2)



'''实例中 dict2 其实是 dict1 的引用（别名），所以输出结果都是一致的，
dict3 父对象进行了深拷贝，不会随dict1 修改而修改，子对象是浅拷贝所以随 dict1 的修改而修改。'''
# dict1 = {'user': 'runoob', 'num': [1, 2, 3]}
# dict2 = dict1  # 浅拷贝: 引用对象
# dict3 = dict1.copy()  # 浅拷贝：深拷贝父对象（一级目录），子对象（二级目录）不拷贝，还是引用
# # 修改 data 数据
# dict1['user'] = 'root'
# dict1['num'].remove(1)
# # 输出结果
# print(dict1)
# print(dict2)
# print(dict3)


'''直接赋值：其实就是对象的引用（别名）。
浅拷贝(copy)：拷贝父对象，不会拷贝对象的内部的子对象。
深拷贝(deepcopy)： copy 模块的 deepcopy 方法，完全拷贝了父对象及其子对象'''

'''字典浅拷贝实例'''
# a = {1: [1,2,3]}
# b = a.copy()
# print(a)
# print(b)
# a[1].append(4)
# print(a)
# print(b)


'''深度拷贝需要引入 copy 模块：'''
# import copy
# a = {1: [1,2,3]}
# a[1].append(4)
# c = copy.deepcopy(a)
# print(a,c)
# a[1].append(5)
# print(a,c)

'''Python 字典 update() 函数把字典参数 dict2 的 key/value(键/值) 对更新到字典 dict 里。
update() 方法语法： dict.update(dict2)'''
# dict = {'Name': 'Runoob', 'Age': 7}
# dict2 = {'Sex': 'female'}
# dict.update(dict2)
# print("更新字典 dict : ", dict)


'''如果键值有重复，则 dict2 的内容更新替换到 dict 中，如上面的代码，会有下面的结果:'''
# dict = {'Name': 'Runoob', 'Age': 7}
# dict2 = {'Age': 'female' }
# dict.update(dict2)
# print ("更新字典 dict : ", dict)

'''按照 key 来给字典排序：'''
# dict = {200:'a',20:'b',610:'c'}
# d1={}
# for k in sorted(dict.keys()):
#     d={k:dict[k]}
#     d1.update(d)
# print(d1)


'''Python 字典 popitem() 方法随机返回并删除字典中的一对键和值(一般删除末尾对)。
如果字典已经为空，却调用了此方法，就报出KeyError异常。'''
site= {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
pop_obj=site.popitem()
print(pop_obj)
print(site)