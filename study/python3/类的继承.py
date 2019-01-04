#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/11/22 21:37

'''继承的定义'''
# class Person(object):  # 定义一个父类
#
#     def talk(self):  # 父类中的方法
#         print("person is talking....")
#
# class Chinese(Person):  # 定义一个子类， 继承Person类
#
#     def walk(self):  # 在子类中定义其自身的方法
#         print('is walking...')
#
# c = Chinese()
# c.talk()  # 调用继承的Person类的方法
# c.walk()  # 调用本身的方法

'''构造函数的继承
继承类的构造方法：
        1.经典类的写法： 父类名称.__init__(self,参数1，参数2，...)
        2. 新式类的写法：super(子类，self).__init__(参数1，参数2，....)'''

'''构造函数的继承'''
# class Person(object):  #定义父类
#     def __init__(self, name, age):   #初始化函数
#         self.name = name              #将属性传给对象
#         self.age = age                  #将属性传给对象
#         self.weight = 'weight'          #将属性传给对象
#
#     def talk(self):
#         print("person is talking....")
#
# class Chinese(Person):   #定义子类
#     def __init__(self, name, age, language):  # 先继承，在重构
#         Person.__init__(self, name, age)  # 继承父类的构造方法，也可以写成：super(Chinese,self).__init__(name,age)
#         self.language = language  # 定义类的本身属性
#
#     def walk(self):
#         print('is walking...')
#
# class American(Person):
#     pass
# c = Chinese('bigberg', 22, 'Chinese')
# c.walk()


'''子类对父类方法的重写
　如果我们对基类/父类的方法需要修改，可以在子类中重构该方法。'''


# class Person(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.weight = 'weight'
#
#     def talk(self):
#         print("person is talking....")
#
#
# class Chinese(Person):
#     def __init__(self, name, age, language):
#         Person.__init__(self, name, age)
#         self.language = language
#         print(self.name, self.age, self.weight, self.language)
#
#     def talk(self):  # 子类 重构方法
#         print('%s is speaking chinese' % self.name)
#
#     def walk(self):
#         print('is walking...')
#
#
# c = Chinese('bigberg', 22, 'Chinese')
# c.talk()

# class Fruit:
#     def __init__(self, color):
#         self.color = color
#         print("fruit's color: %s" % self.color)
#
#     def grow(self):
#         print("grow...")
#
#
# class Apple(Fruit):  # 继承了父类
#     def __init__(self, color):  # 显示调用父类的__init__方法
#         Fruit.__init__(self, color)
#         print("apple's color: %s" % self.color)
#
#
# class Banana(Fruit):  # 继承了父类
#     def __init__(self, color):  # 显示调用父类的__init__方法
#         Fruit.__init__(self, color)
#         print("banana's color:%s" % self.color)
#
#     def grow(self):  # 覆盖了父类的grow方法
#         print("banana grow...")
#
# if __name__ == "__main__":
#     apple = Apple("red")
# apple.grow()
# banana = Banana("yellow")
# banana.grow()



'''
类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；
方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；
通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。
和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：'''
# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#     def get_grade(self):
#         if self.score >= 90:
#             return 'A'
#         elif self.score >= 60:
#             return 'B'
#         else:
#             return 'C'
#
# lisa = Student('Lisa', 99)
# bart = Student('Bart', 59)
# print(lisa.name, lisa.get_grade())#对象调用属性，调用方法
# print(bart.name, bart.get_grade())#对象调用属性，调用方法


class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson', 59)
print('bart.get_name() =', bart.get_name())
bart.set_score(60)
print('bart.get_score() =', bart.get_score())

print('DO NOT use bart._Student__name:', bart._Student__name)
