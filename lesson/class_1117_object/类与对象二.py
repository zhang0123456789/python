#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/11/17 15:11
'''静态方法，创建对象可以调用'''
# class SeniorTestingEngineer:
#     '''属性'''
#     work_year=3
#     salary=20000
#     '''行为   对象方法'''
#     def coding(self,language,a=500):#对象方法，只能由对象调用
#         print("会写{}代码{}行".format(language,a))
#     '''静态方法  对象或不是对象调用都可以'''
#     @staticmethod           #静态方法  不需要特意创建对象来调用  创建对象可以调用不创建也可以调用
#     def do_sql(name):
#         print("会操作{}数据库".format(name))
#
#     def do_linux(self):
#         print("会操作linux系统")
# '''创建对象  类名()
# #1、对象方法的调用 以及静态方法的调用'''
# p1=SeniorTestingEngineer()
# print(p1.salary)
# p1.do_linux()
# p1.do_sql('oracl')
# p1.coding('java')


# class SeniorTestingEngineer:
#     '''属性'''
#     work_year=3
#     salary=20000
#     '''行为   对象方法'''
#     def coding(self,language,a=500):#对象方法，只能由对象调用
#         print("会写{}代码{}行".format(language,a))
#     '''静态方法  对象或不是对象调用都可以'''
#     @staticmethod   #静态方法
#     def do_sql(name):
#         print("会操作{}数据库".format(name))
#     def do_linux(self):
#         print("会操作linux系统")
# '''创建对象  类名()
# #1、对象方法的调用 以及静态方法的调用'''
# p1=SeniorTestingEngineer()
# print(p1.salary)
# p1.do_linux()
# p1.do_sql('oracl')
# p1.coding('java')
#
# '''静态方法staticmethod    直接类名。函数名完成调用   不需要特意创建对象来调用
# 创建对象可以调用不创建也可以调用
# 1、支持对象调用  类.名调用'''
# SeniorTestingEngineer.do_sql('mysql')
# SeniorTestingEngineer().do_sql('mysql')

'''静态方法和类方法 支持对象调用  也支持类名直接调用  '''
# class SeniorTestingEngineer:
#     '''属性'''          #只能对象调用
#     work_year=3
#     salary=20000
#     '''行为   对象方法'''
#     def coding(self,language,a=500):#对象方法，只能由对象调用
#         print("会写{}代码{}行".format(language,a))
#         print("工作年限是{}，月薪是{}".format(self.work_year,self.salary))
#     '''静态方法  对象或不是对象调用都可以'''
    # @staticmethod   #静态方法
    # def do_sql(name):
    #     print("会操作{}数据库".format(name))
    # def do_linux(self):
    #     print("会操作linux系统")
'''创建对象  类名()
#1、对象方法的调用 以及静态方法的调用'''
# p1=SeniorTestingEngineer()
# p1.do_linux()
# p1.do_sql('oracl')
# p1.coding('java')
# print(p1.salary)#调用属性，要用print打印出来

'''静态方法staticmethod    直接类名。函数名完成调用   不需要特意创建对象来调用
创建对象可以调用不创建也可以调用
1、支持对象调用  类.名调用'''
# SeniorTestingEngineer.do_sql('mysql')
# SeniorTestingEngineer().do_sql('mysql')

'''对象方法有self   静态方法有@staticmethod  类方法用@classmethod装饰
2、对象方法可以通过对象self调用类里面的任意属性，静态方法无法调用属性值
3、如果方法跟我们类里面的属性值没有任何关联，就可以写成静态方法
4、共同点：静态方法和类方法 支持对象调用  也支持类名直接调用   对象方法必须对象来调用'''



'''静态方法和类方法 支持对象调用  也支持类名直接调用  '''
# class SeniorTestingEngineer:
#     '''属性'''          #只能对象调用
#     work_year=3
#     salary=20000
#     '''行为   对象方法'''
#     def coding(self,language,a=500):#对象方法，只能由对象调用
#         print("会写{}代码{}行".format(language,a))
#         print("工作年限是{}，月薪是{}".format(self.work_year,self.salary))
#     '''静态方法  对象或不是对象调用都可以'''
#     @staticmethod   #静态方法
#     def do_sql(name):
#         print("会操作{}数据库".format(name))
#     @classmethod     #类方法
#     def do_linux(cls):
#         print("cls的值：",cls)
#         print("会操作linux系统")
# SeniorTestingEngineer.do_linux()
# SeniorTestingEngineer().do_linux()

'''必须通过类.名调用'''
# class SeniorTestingEngineer:
#     '''属性'''          #只能对象调用
#     work_year=3
#     salary=20000
#     '''行为   对象方法'''
#     def coding(self,language,a=500):#对象方法，只能由对象调用
#         print("会写{}代码{}行".format(language,a))
#         print("工作年限是{}，月薪是{}".format(self.work_year,self.salary))
#     '''静态方法  对象或不是对象调用都可以'''
#     @staticmethod   #静态方法
#     def do_sql(name):
#         print("会操作{}数据库".format(name))
#     @classmethod     #类方法
#     def do_linux(cls):
#         # print("cls的值：",cls)
#         print("会操作linux系统")
#         print("工作年限是{}，月薪是{}".format(cls.work_year, cls.salary))
# SeniorTestingEngineer().do_linux()#类方法   创建对象调用
# SeniorTestingEngineer.do_linux()#类方法     不创建对象调用
# print(SeniorTestingEngineer.salary)


'''类方法   位置参数'''
# class SeniorTestingEngineer:
#     '''属性'''          #只能对象调用
#     work_year=3
#     salary=20000
#     '''行为   对象方法'''
#     def coding(self,language,a=500):#对象方法，只能由对象调用
#         print("会写{}代码{}行".format(language,a))
#         print("工作年限是{}，月薪是{}".format(self.work_year,self.salary))
#
#
#     '''静态方法  对象或不是对象调用都可以'''
#     @staticmethod   #静态方法
#     def do_sql(name):
#         print("会操作{}数据库".format(name))
#
#
#     @classmethod     #类方法
#     def do_linux(cls):
#         print("cls的值：",cls)
#         print("会操作linux系统")
#         print("工作年限是{}，月薪是{}".format(cls.work_year, cls.salary))
#     def do_api_testing(self):
#         print("会做接口测试")
# p1=SeniorTestingEngineer().coding("java","5000")


'''类里面的方法编写
1、位置参数  默认参数  动态参数  关键参数  统统都可以加
类里面方法的相互调用
类里面的初始化函数'''


'''类方法            传入动态参数'''
# class SeniorTestingEngineer:
#     '''属性'''          #只能对象调用
#     work_year=3
#     salary=20000
#     '''行为   对象方法'''
#     def coding(self,language,a=500,*args):#对象方法，只能由对象调用
#         print("会写{}代码{}行".format(language,a))
#         print("工作年限是{}，月薪是{}".format(self.work_year,self.salary))
#         print("打印动态参数：{}".format(args))
#
#     '''静态方法  对象或不是对象调用都可以'''
#     @staticmethod   #静态方法
#     def do_sql(name):
#         print("会操作{}数据库".format(name))
#
#
#     @classmethod     #类方法
#     def do_linux(cls):
#         print("cls的值：",cls)
#         print("会操作linux系统")
#         print("工作年限是{}，月薪是{}".format(cls.work_year, cls.salary))
#     def do_api_testing(self):
#         print("会做接口测试")
# p1=SeniorTestingEngineer().coding("java","5000",1,2,3,4,5)



'''类方法       传入关键字参数'''
# class SeniorTestingEngineer:
#     '''属性'''          #只能对象调用
#     work_year=3
#     salary=20000
#     '''行为   对象方法'''
#     def coding(self,language,a=500,*args,**kwargs):#对象方法，只能由对象调用
#         print("会写{}代码{}行".format(language,a))
#         print("工作年限是{}，月薪是{}".format(self.work_year,self.salary))
#         print("打印动态参数：{}".format(args))
#         print("打印动态参数：{}".format(kwargs))
#
#     '''静态方法  对象或不是对象调用都可以'''
#     @staticmethod   #静态方法
#     def do_sql(name):
#         print("会操作{}数据库".format(name))
#
#
#     @classmethod     #类方法
#     def do_linux(cls):
#         print("cls的值：",cls)
#         print("会操作linux系统")
#         print("工作年限是{}，月薪是{}".format(cls.work_year, cls.salary))
#     def do_api_testing(self):
#         print("会做接口测试")
# p1=SeniorTestingEngineer().coding("java","5000",1,2,3,4,5,name='华华',classid='python12')


'''静态方法   传入位置参数、关键字'''
# class SeniorTestingEngineer:
#     '''属性'''          #只能对象调用
#     work_year=3
#     salary=20000
#     '''行为   对象方法'''
#     def coding(self,language,a=500,*args,**kwargs):#对象方法，只能由对象调用
#         print("会写{}代码{}行".format(language,a))
#         print("工作年限是{}，月薪是{}".format(self.work_year,self.salary))
#         print("打印动态参数：{}".format(args))
#         print("打印动态参数：{}".format(kwargs))
#
#     '''静态方法  对象或不是对象调用都可以'''
#     @staticmethod   #静态方法
#     def do_sql(**kwargs):
#         for item in kwargs.values():
#             print("会操作{}数据库".format(item))
#
#
#     @classmethod     #类方法
#     def do_linux(cls):
#         print("cls的值：",cls)
#         print("会操作linux系统")
#         print("工作年限是{}，月薪是{}".format(cls.work_year, cls.salary))
#     def do_api_testing(self):
#         print("会做接口测试")
# SeniorTestingEngineer.do_sql(a='mysql',b='oracle',c='sql server')


'''类方法  传入动态参数'''
# class SeniorTestingEngineer:
#     '''属性'''          #只能对象调用
#     work_year=3
#     salary=20000
#     '''行为   对象方法'''
#     def coding(self,language,a=500,*args,**kwargs):#对象方法，只能由对象调用
#         print("会写{}代码{}行".format(language,a))
#         print("工作年限是{}，月薪是{}".format(self.work_year,self.salary))
#         print("打印动态参数：{}".format(args))
#         print("打印动态参数：{}".format(kwargs))
#
#     '''静态方法  对象或不是对象调用都可以'''
#     @staticmethod   #静态方法
#     def do_sql(**kwargs):
#         for item in kwargs.values():
#             print("会操作{}数据库".format(item))
#
#
#     @classmethod     #类方法
#     def do_linux(cls,name,*args):
#         print("cls的值：",cls)
#         print("会操作linux系统")
#         print("工作年限是{}，月薪是{}".format(cls.work_year, cls.salary))
#         print("类方法里面的动态参数：",args)
#     def do_api_testing(self):
#         print("会做接口测试")
# SeniorTestingEngineer.do_linux("linux",1,2,3,4,5)

'''类方法  return  与普通函数的return是一样的
需要的时候返回值的时候就写  '''
# class SeniorTestingEngineer:
#     '''属性'''          #只能对象调用
#     work_year=3
#     salary=20000
#     '''行为   对象方法'''
#     def coding(self,language,a=500,*args,**kwargs):#对象方法，只能由对象调用
#         print("会写{}代码{}行".format(language,a))
#         print("工作年限是{}，月薪是{}".format(self.work_year,self.salary))
#         print("打印动态参数：{}".format(args))
#         print("打印动态参数：{}".format(kwargs))
#
#     '''静态方法  对象或不是对象调用都可以'''
#     @staticmethod   #静态方法
#     def do_sql(**kwargs):
#         for item in kwargs.values():
#             print("会操作{}数据库".format(item))
#
#
#     @classmethod     #类方法
#     def do_linux(cls,name,*args):
#         print("cls的值：",cls)
#         print("会操作linux系统")
#         print("工作年限是{}，月薪是{}".format(cls.work_year, cls.salary))
#         return ("类方法里面的动态参数：",args)
#
#
#     def do_api_testing(self):
#         print("会做接口测试")
# t=SeniorTestingEngineer.do_linux("linux",1,2,3,4,5)
# print(t)








'''类方法   retrun 不需要返回的时候就return空,,none'''
# class SeniorTestingEngineer:
#     '''属性'''          #只能对象调用
#     work_year=3
#     salary=20000
#     '''行为   对象方法'''
#     def coding(self,language,a=500,*args,**kwargs):#对象方法，只能由对象调用
#         print("会写{}代码{}行".format(language,a))
#         print("工作年限是{}，月薪是{}".format(self.work_year,self.salary))
#         print("打印动态参数：{}".format(args))
#         print("打印动态参数：{}".format(kwargs))
#
#     '''静态方法  对象或不是对象调用都可以'''
#     @staticmethod   #静态方法
#     def do_sql(**kwargs):
#         for item in kwargs.values():
#             print("会操作{}数据库".format(item))
#
#
#     @classmethod     #类方法
#     def do_linux(cls,name,*args):
#         print("cls的值：",cls)
#         print("会操作linux系统")
#         print("工作年限是{}，月薪是{}".format(cls.work_year, cls.salary))
#         return
#
#     def do_api_testing(self):
#         print("会做接口测试")
# t=SeniorTestingEngineer.do_linux("linux",1,2,3,4,5)
# print(t)

'''返回一个参数'''
# class SeniorTestingEngineer:
#     '''属性'''          #只能对象调用
#     work_year=3
#     salary=20000
#     '''行为   对象方法'''
#     def coding(self,language,a=500,*args,**kwargs):#对象方法，只能由对象调用
#         print("会写{}代码{}行".format(language,a))
#         print("工作年限是{}，月薪是{}".format(self.work_year,self.salary))
#         print("打印动态参数：{}".format(args))
#         print("打印动态参数：{}".format(kwargs))
#
#     '''静态方法  对象或不是对象调用都可以'''
#     @staticmethod   #静态方法
#     def do_sql(**kwargs):
#         for item in kwargs.values():
#             print("会操作{}数据库".format(item))
#
#
#     @classmethod     #类方法
#     def do_linux(cls,name,*args):
#         print("cls的值：",cls)
#         print("会操作linux系统")
#         print("工作年限是{}，月薪是{}".format(cls.work_year, cls.salary))
#         return  "类方法里面的动态参数{}：" .format(args)
#
#     def do_api_testing(self):
#         print("会做接口测试")
# t=SeniorTestingEngineer.do_linux("linux",1,2,3,4,5)
# print(t)

'''函数之间的调用'''
# class SeniorTestingEngineer:
#     '''属性'''          #只能对象调用
#     work_year=3
#     salary=20000
#     '''行为   对象方法'''
#     def coding(self,language,a=500,*args,**kwargs):#对象方法，只能由对象调用
#         print("会写{}代码{}行".format(language,a))
#         print("工作年限是{}，月薪是{}".format(self.work_year,self.salary))
#         print("打印动态参数：{}".format(args))
#         print("打印动态参数：{}".format(kwargs))
#         self.do_function_testing()
#
#     '''静态方法  对象或不是对象调用都可以'''
#     @staticmethod   #静态方法
#     def do_sql(**kwargs):
#         for item in kwargs.values():
#             print("会操作{}数据库".format(item))
#
#
#     @classmethod     #类方法
#     def do_linux(cls,name,*args):
#         print("cls的值：",cls)
#         print("会操作linux系统")
#         print("工作年限是{}，月薪是{}".format(cls.work_year, cls.salary))
#         return  "类方法里面的动态参数{}：" .format(args)
#
#     def do_function_testing(self):
#         print("会做接口测试")
# p4=SeniorTestingEngineer()
# p4.coding("java",'5000',1,2,3,4,5,name='huahua',classid='python12')

'''函数之间的调用'''
# class SeniorTestingEngineer:
#     '''属性'''          #只能对象调用
#     work_year=3
#     salary=20000
#     '''行为   对象方法'''
#     def coding(self,language,a=500,*args,**kwargs):#对象方法，只能由对象调用
#         print("会写{}代码{}行".format(language,a))
#         print("工作年限是{}，月薪是{}".format(self.work_year,self.salary))
#         print("打印动态参数：{}".format(args))
#         print("打印动态参数：{}".format(kwargs))
#         self.do_function_testing('C\S客户端')
#
#     '''静态方法  对象或不是对象调用都可以'''
#     @staticmethod   #静态方法
#     def do_sql(**kwargs):
#         for item in kwargs.values():
#             print("会操作{}数据库".format(item))
#
#
#     @classmethod     #类方法
#     def do_linux(cls,name,*args):
#         print("cls的值：",cls)
#         print("会操作linux系统")
#         print("工作年限是{}，月薪是{}".format(cls.work_year, cls.salary))
#         return  "类方法里面的动态参数{}：" .format(args)
#
#     def do_function_testing(self,type):
#         print("会做{}接口测试".format(type))

# p4=SeniorTestingEngineer()
# p4.coding("java",'5000',1,2,3,4,5,name='huahua',classid='python12')


# class SeniorTestingEngineer:
#     '''属性'''          #只能对象调用
#     work_year=3
#     salary=20000
#     '''行为   对象方法'''
#     def coding(self,language,type,a=500,*args,**kwargs):#对象方法，只能由对象调用
#         print("会写{}代码{}行".format(language,a))
#         print("工作年限是{}，月薪是{}".format(self.work_year,self.salary))
#         print("打印动态参数：{}".format(args))
#         print("打印动态参数：{}".format(kwargs))
#         self.do_function_testing(type)
#
#     '''静态方法  对象或不是对象调用都可以'''
#     @staticmethod   #静态方法
#     def do_sql(**kwargs):
#         for item in kwargs.values():
#             print("会操作{}数据库".format(item))


    # @classmethod     #类方法
    # def do_linux(cls,name,*args):
    #     print("cls的值：",cls)
    #     print("会操作linux系统")
    #     print("工作年限是{}，月薪是{}".format(cls.work_year, cls.salary))
    #     return  "类方法里面的动态参数{}：" .format(args)
    #
    # def do_function_testing(self,type):
    #     print("会做{}接口测试".format(type))


# p1=SeniorTestingEngineer().coding("java","5000",1,2,3,4,5,name='huahua',classid='python12')
# SeniorTestingEngineer.do_sql(a='mysql',b='oracle',c='sql server')
# t=SeniorTestingEngineer.do_linux("linux",1,2,3,4,5)
# print(t)
# p4=SeniorTestingEngineer()
# p4.coding("java",'web','5000',1,2,3,4,5,name='huahua',classid='python12')