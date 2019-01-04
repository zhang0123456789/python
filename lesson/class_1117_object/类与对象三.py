#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time :2018/11/17 15:11
# class SeniorTestingEngineer:
#     '''属性'''  # 只能对象调用
#     work_year = 3
#     salary = 20000
#     '''行为   对象方法'''
#
#     def coding(self, language,type, a=500, *args, **kwargs):  # 对象方法，只能由对象调用
#         print("会写{}代码{}行".format(language, a))
#         print("工作年限是{}，月薪是{}".format(self.work_year, self.salary))
#         print("打印动态参数：{}".format(args))
#         print("打印动态参数：{}".format(kwargs))
#         self.do_function_testing(type)  #调用对象方法
#         self.do_linux('linux')   #调用类方法
#     '''静态方法  对象或不是对象调用都可以'''
#
#     @staticmethod  # 静态方法
#     def do_sql(**kwargs):
#         for item in kwargs.values():
#             print("会操作{}数据库".format(item))
#
#     @classmethod  # 类方法
#     def do_linux(cls, name):
#         print("会操作{}系统".format(name))
#
#     def do_function_testing(self, type):
#         print("会做{}接口测试".format(type))
# p5=SeniorTestingEngineer()
# p5.coding("java",'web','5000',1,2,3,4,5,name='huahua',classid='python12')


'''===================对象方法里面  调用对象方法  静态方法  类方法==================='''
# class SeniorTestingEngineer:
#     '''属性'''  # 只能对象调用
#     work_year = 3
#     salary = 20000
#     '''行为   对象方法'''
#
#     def coding(self, language, type, a=500, *args, **kwargs):  # 对象方法，只能由对象调用
#         print("会写{}代码{}行".format(language, a))
#         print("工作年限是{}，月薪是{}".format(self.work_year, self.salary))
#         print("打印动态参数：{}".format(args))
#         print("打印动态参数：{}".format(kwargs))
#         self.do_function_testing(type)  #调用对象方法
#         self.do_linux('linux')   #调用类方法
#         self.do_sql(a='mysql')   #调用静态方法
#
#     '''静态方法  对象或不是对象调用都可以'''
#
#     @staticmethod  # 静态方法
#     def do_sql(**kwargs):
#         for item in kwargs.values():
#             print("会操作{}数据库".format(item))
#
#     @classmethod  # 类方法
#     def do_linux(cls, name):
#         print("会操作{}系统".format(name))
#
#     def do_function_testing(self, type):
#         print("会做{}接口测试".format(type))
# p5=SeniorTestingEngineer()
# p5.coding("java",'web','5000',1,2,3,4,5,name='huahua',classid='python12')



'''=====================对象方法调用 对象方法==========================='''
# class SeniorTestingEngineer:
#     '''属性'''  # 只能对象调用
#     work_year = 3
#     salary = 20000
#     '''行为   对象方法'''
#
#     def coding(self, type,language):  # 对象方法，只能由对象调用
#         print("会写{}代码".format(language))
#         self.do_function_testing(type)  #调用对象方法
#
#
#     '''静态方法  对象或不是对象调用都可以'''
#
#     @staticmethod  # 静态方法
#     def do_sql(name):
#             print("会操作{}数据库".format(name))
#
#     @classmethod  # 类方法
#     def do_linux(cls, name):
#         print("会操作{}系统".format(name))
#
#     def do_function_testing(self, name):  #对象方法
#         print("会做{}接口测试".format(name))
# p1=SeniorTestingEngineer()
# p1.coding('APP','python')


'''==================对象方法调用静态方法=================='''
# class SeniorTestingEngineer:
#     '''属性'''  # 只能对象调用
#     work_year = 3
#     salary = 20000
#     '''行为   对象方法'''
#
#     def coding(self, language):  # 对象方法，只能由对象调用
#         print("会写{}代码".format(language))
#         self.do_sql('mysql')  #调用静态方法
#
#
#     '''静态方法  对象或不是对象调用都可以'''
#
#     @staticmethod  # 静态方法
#     def do_sql(name):
#             print("静态方法，会操作{}数据库".format(name))
#
#     @classmethod  # 类方法
#     def do_linux(cls, name):
#         print("类方法，会操作{}系统".format(name))
#
#     def do_function_testing(self, type):  #对象方法
#         print("会做{}接口测试".format(type))
# p1=SeniorTestingEngineer()
# p1.coding('python')

'''==================对象方法调用类方法==============='''
# class SeniorTestingEngineer:
#     '''属性'''  # 只能对象调用
#     work_year = 3
#     salary = 20000
#     '''行为   对象方法'''
#
#     def coding(self, language):  # 对象方法，只能由对象调用
#         print("会写{}代码".format(language))
#         self.do_linux('linux') #调用类方法
#
#
#     '''静态方法  对象或不是对象调用都可以'''
#
#     @staticmethod  # 静态方法
#     def do_sql(name):
#             print("静态方法，会操作{}数据库".format(name))
#
#     @classmethod  # 类方法
#     def do_linux(cls, name):
#         print("类方法，会操作{}系统".format(name))
#
#     def do_function_testing(self, type):  #对象方法
#         print("对象方法，会做{}接口测试".format(type))
# p1=SeniorTestingEngineer()
# p1.coding('python')


'''对象方法有self   静态方法有@staticmethod  类方法用@classmethod装饰
2、对象方法可以通过对象self调用类里面的任意属性，静态方法无法调用属性值
3、如果方法跟我们类里面的属性值没有任何关联，就可以写成静态方法
4、共同点：静态方法和类方法 支持对象调用  也支持类名直接调用   对象方法必须对象来调用'''

'''====================对象方法里面   直接用类名调用静态方法========================='''
# class SeniorTestingEngineer:
#     '''属性'''  # 只能对象调用
#     work_year = 3
#     salary = 20000
#     '''行为   对象方法'''
#
#     def coding(self, language):  # 对象方法，只能由对象调用
#         print("会写{}代码".format(language))
#         SeniorTestingEngineer.do_sql('sql.server')
#
#     '''静态方法  对象或不是对象调用都可以'''
#     @staticmethod  # 静态方法
#     def do_sql(name):
#             print("静态方法，会操作{}数据库".format(name))
#
#     @classmethod  # 类方法
#     def do_linux(cls, name):
#         print("类方法，会操作{}系统".format(name))
#
#     def do_function_testing(self, type):  #对象方法
#         print("对象方法，会做{}接口测试".format(type))
# p1=SeniorTestingEngineer()
# p1.coding('python')


# '''==============对象方法里面  直接用类名调用类方法==========================='''
# class SeniorTestingEngineer:
#     '''属性'''  # 只能对象调用
#     work_year = 3
#     salary = 20000
#     '''行为   对象方法'''
#
#     def coding(self, language):  # 对象方法，只能由对象调用
#         print("会写{}代码".format(language))
#         SeniorTestingEngineer.do_linux('linux')
#
#     '''静态方法  对象或不是对象调用都可以'''
#     @staticmethod  # 静态方法
#     def do_sql(name):
#             print("静态方法，会操作{}数据库".format(name))
#
#     @classmethod  # 类方法
#     def do_linux(cls, name):
#         print("类方法，会操作{}系统".format(name))
#
#     def do_function_testing(self, type):  #对象方法
#         print("对象方法，会做{}接口测试".format(type))
# p1=SeniorTestingEngineer()
# p1.coding('python')
#
#
# '''===================静态方法里面调用对象方法====================='''
# class SeniorTestingEngineer:
#     '''属性'''  # 只能对象调用
#     work_year = 3
#     salary = 20000
#     '''行为   对象方法'''
#
#     def coding(self, language):  # 对象方法，只能由对象调用
#         print("会写{}代码".format(language))
#
#
#     '''静态方法  对象或不是对象调用都可以'''
#     @staticmethod  # 静态方法
#     def do_sql(name):
#             print("静态方法，会操作{}数据库".format(name))
#             SeniorTestingEngineer().do_function_testing('web')
#
#     @classmethod  # 类方法
#     def do_linux(cls, name):
#         print("类方法，会操作{}系统".format(name))
#
#     def do_function_testing(self, type):  #对象方法
#         print("对象方法，会做{}接口测试".format(type))
# p1=SeniorTestingEngineer()
# p1.do_sql('oracle')
#
#
# '''===============静态方法里面调用类方法================='''
# class SeniorTestingEngineer:
#     '''属性'''  # 只能对象调用
#     work_year = 3
#     salary = 20000
#     '''行为   对象方法'''
#
#     def coding(self, language):  # 对象方法，只能由对象调用
#         print("会写{}代码".format(language))
#
#
#     '''静态方法  对象或不是对象调用都可以'''
#     @staticmethod  # 静态方法
#     def do_sql(name):
#             print("静态方法，会操作{}数据库".format(name))
#
#             SeniorTestingEngineer.do_linux('windows')
#     @classmethod  # 类方法
#     def do_linux(cls, name):
#         print("类方法，会操作{}系统".format(name))
#
#     def do_function_testing(self, type):  #对象方法
#         print("对象方法，会做{}接口测试".format(type))
# p1=SeniorTestingEngineer()
# p1.do_sql('oracle')


'''==========================类方法调用类方法============================='''
# class SeniorTestingEngineer:
#     '''属性'''  # 只能对象调用
#     work_year = 3
#     salary = 20000
#     '''行为   对象方法'''
#
#     def coding(self, language):  # 对象方法，只能由对象调用
#         print("会写{}代码".format(language))
#
#
#     '''静态方法  对象或不是对象调用都可以'''
#     @staticmethod  # 静态方法
#     def do_sql(name):
#             print("静态方法，会操作{}数据库".format(name))
#
#     @classmethod  # 类方法
#     def do_linux(cls, name):
#         cls.do_function_testing('手机')
#         print("类方法，会操作{}系统".format(name))
#
#     @classmethod    # 类方法
#     def do_function_testing(self, type):  #对象方法
#         print("类方法方法，会做{}功能测试".format(type))
# p1=SeniorTestingEngineer()
# p1.do_linux('centos')
#
#
#
'''====================类方法调用类方法=============================='''
# class SeniorTestingEngineer:
#     '''属性'''  # 只能对象调用
#     work_year = 3
#     salary = 20000
#     '''行为   对象方法'''
#
#     def coding(self, language):  # 对象方法，只能由对象调用
#         print("会写{}代码".format(language))
#
#
#     '''静态方法  对象或不是对象调用都可以'''
#     @staticmethod  # 静态方法
#     def do_sql(name):
#             print("静态方法，会操作{}数据库".format(name))
#
#     @classmethod  # 类方法
#     def do_linux(cls, name):
#         cls().do_function_testing('手机')
#         print("类方法，会操作{}系统".format(name))
#
#     @classmethod    # 类方法
#     def do_function_testing(self, type):  #对象方法
#         print("类方法，会做{}功能测试".format(type))
# p1=SeniorTestingEngineer()
# p1.do_linux('centos')



'''使用初始化函数，在创建对象的时候，就要传入参数  参数要一一对应'''
# class SeniorTestingEngineer:
#     '''属性'''  # 只能对象调用
#     def __init__(self,work_year,salary):
#         self.work_year=work_year
#         self.salary=salary
#     '''行为   对象方法'''
#     def coding(self,language):  # 对象方法，只能由对象调用
#         print("会写{}代码".format(language))
#         print("工作经验{}，月薪是{}".format(self.work_year,self.salary))
#     '''静态方法  对象或不是对象调用可以'''
#     @staticmethod  # 静态方法
#     def do_sql(name):
#             print("静态方法，会操作{}数据库".format(name))
#     @classmethod  # 类方法
#     def do_linux(cls, name):
#         print("类方法，会操作{}系统".format(name))
#     def do_function_testing(self, type):  #对象方法
#         print("类方法，会做{}功能测试".format(type))
# p1=SeniorTestingEngineer(4,40000)
# p1.coding('java')


'''传入多个参数'''
class SeniorTestingEngineer:
    '''属性'''  # 只能对象调用
    def __init__(self,name,work_year,salary):
        self.work_year=work_year
        self.salary=salary
        self.name=name
    '''行为   对象方法'''
    def coding(self,language):  # 对象方法，只能由对象调用
        print("会写{}代码".format(language))
        print("{}同学，工作经验{}，月薪是{}".format(self.name,self.work_year,self.salary))
    '''静态方法  对象或不是对象调用可以'''
    @staticmethod  # 静态方法
    def do_sql(name):
            print("静态方法，会操作{}数据库".format(name))
    @classmethod  # 类方法
    def do_linux(cls, name):
        print("类方法，会操作{}系统".format(name))
    def do_function_testing(self, type):  #对象方法
        print("类方法，会做{}功能测试".format(type))
p1=SeniorTestingEngineer("huahua",4,40000)
p1.coding('java')

p2=SeniorTestingEngineer("娜娜",2,20000)
p2.coding('ruby')

SeniorTestingEngineer.do_sql('mysql')

# class 类():
#     def __init__(self,参数):    # 把第一个带init的def比喻为没有key值的字典，参数比喻为value
#         self.参数1=参数1            # 把参数1赋值给self.参数1，这样其他函数（def）就可以调用
#     def 函数1(self):              # 第二个def相当于对第一个字典进行操作（增删改查）
#         print(self.参数1+"我是菜鸟")    # 拼接输出，调用了第一个def的参数1
# 输出=类("print")                        # 给第一个def字典赋值
# 输出.函数1()                            # 调用第二个def


