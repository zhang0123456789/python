#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/11/17 12:03
'''编码问题 encode decode  不同编码之间的转化'''
# s='柠檬班12期'
# print(s.encode('gbk'))  #gbk编码  b'\xc4\xfb\xc3\xca\xb0\xe012\xc6\xda'
#
# s='柠檬班12期'
# print(s.encode('gbk').decode('gbk').encode('utf-8'))  #gbk解码b'\xe6\x9f\xa0\xe6\xaa\xac\xe7\x8f\xad12\xe6\x9c\x9f'

'''
为了处理英文字符，产生了ASCII码   英文占1个字符，中文占3个字符
为了处理中文字符，产生了GB2312（GBK）
为了处理各国字符，产生了unicode
为了提高Unicode存储和传输性能，产生了UTF-8，他是unicode的一种实现形式
操作系统是unicode编码     格式：内容.encode(编码)'''

'''冒泡算法'''
# L=[98,7,66,1,4]  #[1,4,7,66,98]
#比较n-1轮，元素之间  俩俩比较
#每一轮比较中  都是俩俩相邻比较  从第一个元素开始比较  根据大小去交换位置
# for i in range(0,len(L)-1):  #控制次数0 1 2 3
#     for j in range(0,len(L)-1):
#         if L[j]>L[j+1]:
#             L[j],L[j+1]=L[j+1],L[j]
# print(L)

# L=[98,7,66,1,4]  #[1,4,7,66,98]
# for i in range(0,len(L)-1):  #控制次数0 1 2 3
#     for j in range(0,len(L)-1-i):
#         if L[j]>L[j+1]:
#             L[j],L[j+1]=L[j+1],L[j]
# print(L)

# L=[98,7,66,1,4,9,3,2]
# for i in range(0,len(L)-1):
#     for j in range(0,len(L)-1):
#         if L[j]>L[j+1]:
#             L[j],L[j+1]=L[j+1],L[j]
# print(L)
#
# L=[98,7,66,1,4,9,3,2]
# for i in range(0,len(L)-1):
#     for j in range(0,len(L)-1-i):
#         if L[j]>L[j+1]:
#             L[j],L[j+1]=L[j+1],L[j]
# print(L)

'''文件的关闭以及上下文的管理器'''
# file=open('python12.txt','w+')
# print(file.closed)   #判断文件是否已关闭

# file.close()  #关闭文件
# print(file.closed)    #判断文件是否已关闭

'''上下文管理器    在as下面不做任何操作，，脱离as,自动关闭文件'''
# with open("python12.txt",'w+') as file:
#     print(file.closed)
#
# print(file.closed)

'''文件的数据写入  writelines'''
# with open("python12.txt", 'w+',encoding='utf-8') as file:
#     s=['A组组长是谁！\n','B组的大佬们']  #\n是换行
#     file.writelines(s)  #传入一个列表

# with open("python12.txt", 'w+', encoding='utf-8') as file:
#      s = ['A组组长是谁！', 'B组的大佬们']  # \n是换行
#      file.writelines(s)

'''异常处理     抓到异常 然后做出相关处理
try...except...
代码从上往下执行'''

# a=10
# print(a+b)   #提示  NameError: name 'b' is not defined
# with open("python12.txt", 'w+', encoding='utf-8') as file:
#     file.write("python12期真的666的")  #前面的报错，，导致下面的代码无法进行


# with open("python12.txt",  encoding='utf-8') as file:
#     file.write("python12期真的666的")  #提示io.UnsupportedOperation: not writable
# a=10
# b=20
# print(a+b)

'''代码错误，则处理，执行except后面的代码'''
# try:  #监控可疑代码
#     with open("python12.txt",encoding='utf-8') as file:
#         file.write("python12期真的666的")
# except:  #处理错误  只有代码出错，才会执行except后面的代码
#     print("出错啦！！")
# a=10
# b=20
# print(a+b)

# '''代码正确，则不处理，直接执行'''
# try:  #监控可疑代码
#     with open("python12.txt", 'w+' ,encoding='utf-8') as file:
#         file.write("python12期真的666的")
# except:  #处理
#     print("出错啦！！")
# a=10
# b=20
# print(a+b)


'''抓到了错误代码类型'''
# try:  #监控可疑代码
#     with open("python12.txt",encoding='utf-8') as file:
#         file.write("python12期真的666的")
# except Exception as e:  #处理
#     print("出错:{}！！".format(e))
#
# a=10
# print(a+b)


'''监控多个代码'''
# try:  #监控可疑代码
#     with open("python12.txt",encoding='utf-8') as file:
#         file.write("python12期真的666的")
# except Exception as e:  #处理
#     print("出错:{}！！".format(e))
# try:
#     a=10
#     print(a+b)
# except Exception as c:
#     print("出错：{}".format(c))

'''#只抓指定类型的错误'''
# a=10
# try:
#     print(a+b)
# except NameError as e:  #只抓指定类型的错误
#     print("报错了：{}".format(e))


# a=10
# try:
#     print(a+b)
# except TimeoutError as e:  #只抓指定类型的错误
#     print("报错了：{}".format(e))

# L=[1,2,3]
# print(L[4])   #IndexError: list index out of range

# d={'name':'huahua','age':18}
# print(d['sex'])   #KeyError: 'sex'


'''try下面可以放多行代码   代码从上往下  遇到一个错误就处理，不执行下面其他代码了'''
# a=10
# try:
#     print(a+b)
#     L=[1,2,3]
#     print(L[4])
# except IOError as e:
#     print("报错了：{}".format(e))
# except NameError as e:  #只抓指定类型的错误
#     print("报错了：{}".format(e))
# except IndexError as e:
#     print("报错了：{}".format(e))


'''便于精确错误在哪里'''
# a=10
# try:
#     print(a+b)
# except IOError as e:
#     print("报错了：{}".format(e))
# except NameError as e:  #只抓指定类型的错误
#     print("报错了：{}".format(e))

# try:
#     d = {'name': 'huahua', 'age': 18}
#     print(d['sex'])
# except KeyError as e:
#     print("报错了：{}".format(e))


# try:
#     d = {'name': 'huahua', 'age': 18}
#     print(d['sex'])
# except KeyError as e:
#     print("报错了：{}".format(e))
# finally:  #不管上面报不报错怎么样  都会执行下面的代码
#         a=10
#         b=20
#         print(a+b)

'''#当try后面的代码没有问题 就执行else,否则不执行'''
# try:
#     d = {'name': 'huahua', 'age': 18}
#     print(d['sex'])
# except KeyError as e:
#     print("报错了：{}".format(e))
# else:  #当try后面的代码没有问题 就执行else,否则不执行
#         a=10
#         b=20
#         print(a+b)
#
# try:
#     d = {'name': 'huahua', 'age': 18}
#     print(d['age'])
# except KeyError as e:
#     print("报错了：{}".format(e))
# else:  #当try后面的代码没有问题 就执行else,否则不执行
#         a=10
#         b=20
#         print(a+b)


'''类'''
#自动化测试工程师类
#work_year=3
#salary=20000
#skill:会写代码  会sql  会linux  会功能测试 会自动化测试  会接口测试

'''python类的语法
关键字  class
class  类名  #类名的规范  不能用关键字  驼峰命名AtudyPython
属性：即变量
行为：即函数'''

# class SeniorTestingEngineer:
#     '''属性'''
#     work_year=3
    # salary=20000
    # '''行为'''
    # def coding(self):
    #     print("会写代码")
    # def do_sql(self):
    #     print("会操作数据库")
    # def do_linux(self):
    #     print("会操作linux系统")
    # def do_function_testing(self):
    #     print("会功能测试")
    # def do_api_testing(self):
    #     print("会做接口测试")

#万物皆对象
#克隆一个符合规则的个体
'''创造一个对象    类名()'''
# p1=SeniorTestingEngineer()
# p2=SeniorTestingEngineer()
# p3=SeniorTestingEngineer()
'''对象拥有类里面的所有属性和函数的使用权  类里面的函数只能由对象调用'''
# p1.do_api_testing()
# p2.do_sql()
# p3.do_linux()  #拿到函数 就等于调用函数
# print(p3.salary)  #直接打印出来


'''self存放的内存地址'''
# class SeniorTestingEngineer:
#     '''属性'''
#     work_year=3
#     salary=20000
#     '''行为'''
#     def coding(self):#对象方法，只能由对象调用
#         print("此处打印self:",self)  #此处打印self <__main__.SeniorTestingEngineer object at 0x00000000023B0518>
#         # print("会写代码")
#     def do_sql(self):
#         print("会操作数据库")
#     def do_linux(self):
#         print("会操作linux系统")
#     def do_function_testing(self):
#         print("会功能测试")
#     def do_api_testing(self):
#         print("会做接口测试")
# p1=SeniorTestingEngineer()
# print("此处打印p1:",p1)  #此处打印p1: <__main__.SeniorTestingEngineer object at 0x00000000023B0518>
# p1.coding()

'''添加一个变量'''
# class SeniorTestingEngineer:
#     '''属性'''
#     work_year=3
#     salary=20000
#     '''行为'''
#     def coding(self,language):#对象方法，只能由对象调用
#         print("此处打印self:",self)
#         print("会写{}代码".format(language))
#     def do_sql(self):
#         print("会操作数据库")
#     def do_linux(self):
#         print("会操作linux系统")
#     def do_function_testing(self):
#         print("会功能测试")
#     def do_api_testing(self):
#         print("会做接口测试")
# p1=SeniorTestingEngineer()
# print("此处打印p1:",p1)
# p1.coding('python')#  传入一个参数  #打印出：会写python代码


'''添加多个变量'''
# class SeniorTestingEngineer:
#     '''属性'''
#     work_year=3
#     salary=20000
#     '''行为'''
#     def coding(self,language,a):#对象方法，只能由对象调用
#         print("此处打印self:",self)
#         print("会写{}代码{}行".format(language,a))
#     def do_sql(self):
#         print("会操作数据库")
#     def do_linux(self):
#         print("会操作linux系统")
#     def do_function_testing(self):
#         print("会功能测试")
#     def do_api_testing(self):
#         print("会做接口测试")
# p1=SeniorTestingEngineer()
# print("此处打印p1:",p1)
# p1.coding('python',500)#  传入多个参数  #打印出：会写python代码500行


'''添加多个变量  默认参数'''
# class SeniorTestingEngineer:
#     '''属性'''
#     work_year=3
#     salary=20000
#     '''行为   对象方法'''
#     def coding(self,language,a=500):#对象方法，只能由对象调用
#         # print("此处打印self:",self)
#         print("会写{}代码{}行".format(language,a))
#     def do_sql(self):
#         print("会操作数据库")
#     def do_linux(self):
#         print("会操作linux系统")
#     def do_function_testing(self):
#         print("会功能测试")
#     def do_api_testing(self):
#         print("会做接口测试")
# p1=SeniorTestingEngineer()
# # print("此处打印p1:",p1)
# p1.coding("python")


'''添加多个变量  '''
# class SeniorTestingEngineer:
#     '''属性'''
#     work_year=3
#     salary=20000
#     '''行为   对象方法'''
#     def coding(self,language,a):#对象方法，只能由对象调用
#         # print("此处打印self:",self)
#         print("会写{}代码{}行".format(language,a))
#     def do_sql(self):
#         print("会操作数据库")
#     def do_linux(self):
#         print("会操作linux系统")
#     def do_function_testing(self):
#         print("会功能测试")
#     def do_api_testing(self):
#         print("会做接口测试")
# p1=SeniorTestingEngineer()
# # print("此处打印p1:",p1)
# p1.coding("python",8888888)


'''以类名调用  就得传入对象  默认参数'''
# class SeniorTestingEngineer:
#     '''属性'''
#     work_year=3
#     salary=20000
#     '''行为'''
#     def coding(self,language,a=500):#对象方法，只能由对象调用
#         # print("此处打印self:",self)
#         print("会写{}代码{}行".format(language,a))
#     def do_sql(self):
#         print("会操作数据库")
#     def do_linux(self):
#         print("会操作linux系统")
#     def do_function_testing(self):
#         print("会功能测试")
#     def do_api_testing(self):
#         print("会做接口测试")
#
# p1=SeniorTestingEngineer  #没有()没有创建对象
# # print("此处打印p1:",p1)
# p1.coding(SeniorTestingEngineer(),'python')#  传入多个参数  #打印出：会写python代码500行
#
# p2=SeniorTestingEngineer() #有()，创建对象
# p2.coding('java')


'''以类名调用  就得传入对象  '''
# class SeniorTestingEngineer:
#     '''属性'''
#     work_year=3
#     salary=20000
#     '''行为'''
#     def coding(self,language,a=500):#对象方法，只能由对象调用
#         # print("此处打印self:",self)
#         print("会写{}代码{}行".format(language,a))
#     def do_sql(self):
#         print("会操作数据库")
#     def do_linux(self):
#         print("会操作linux系统")
#     def do_function_testing(self):
#         print("会功能测试")
#     def do_api_testing(self):
#         print("会做接口测试")
#
# p1=SeniorTestingEngineer  #没有()没有创建对象
# # print("此处打印p1:",p1)
# p1.coding(SeniorTestingEngineer(),'python',9999999999999999999999)#  传入多个参数  #打印出：会写python代码99999999999999999999行
#
# p2=SeniorTestingEngineer() #有()，创建对象
# p2.coding('java')



'''静态方法  对象可以调用'''
# class SeniorTestingEngineer:
#     '''属性'''
#     work_year=3
#     salary=20000
#     '''行为'''
#     def coding(self,language,a=500):#对象方法，只能由对象调用
#         # print("此处打印self:",self)
#         print("会写{}代码{}行".format(language,a))
#     '''静态方法'''
#     @staticmethod
#     def do_sql(name):
#         print("会操作{}数据库".format(name))
#     def do_linux(self):
#         print("会操作linux系统")
#     def do_function_testing(self):
#         print("会功能测试")
#     def do_api_testing(self):
#         print("会做接口测试")
# p1=SeniorTestingEngineer()
# p1.coding("python")
# p1.do_sql("mysql")

'''静态方法  不创建对象也可以调用'''
# class SeniorTestingEngineer:
#     '''属性'''
#     work_year=3
#     salary=20000
#     '''行为'''
#     def coding(self,language,a=500):#对象方法，只能由对象调用
#         # print("此处打印self:",self)
#         print("会写{}代码{}行".format(language,a))
#     '''静态方法  对象或不是对象调用都可以'''
#     @staticmethod
#     def do_sql(name):
#         print("会操作{}数据库".format(name))
#     def do_linux(self):
#         print("会操作linux系统")
#     def do_function_testing(self):
#         print("会功能测试")
#     def do_api_testing(self):
#         print("会做接口测试")
# p1=SeniorTestingEngineer
# p1.coding(SeniorTestingEngineer(),"python")
# p1.do_sql("mysql")

'''类函数内调用不带参数的类函数   不传参数'''
class SuperMan:
    #类的属性
    age=30
    sex='male'
    name='nick'

    #类的方法
    def protect_people(self,name='毛毛'):
        print("我是超人，我会保护人民，我的名字叫：{}".format(name))
        self.fly_to_sky()#调用类函数fly_to_sky

    def fly_to_sky(self):
        print("我是超人，我可以上天")
person=SuperMan()
person.protect_people()#不传参数
#打印     我是超人，我会保护人民，我的名字叫：毛毛
#打印     我是超人，我可以上天

'''类函数内调用不带参数的类函数   传参数'''
# class SuperMan:
#     #类的属性
#     age=30
#     sex='male'
#     name='nick'
#
#     #类的方法
#     def protect_people(self,name='毛毛'):
#         print("我是超人，我会保护人民，我的名字叫：{}".format(name))
#         self.fly_to_sky()#调用类函数fly_to_sky
#
#     def fly_to_sky(self):
#         print("我是超人，我可以上天")
# person=SuperMan()
# person.protect_people("华华")#传入参数
#打印     我是超人，我会保护人民，我的名字叫：华华
#打印     我是超人，我可以上天


'''类函数内调用带参数的类函数'''
# class SuperMan:
#     #类的属性
#     age=30
#     sex='male'
#     name='nick'
#     #类的方法
#     def protect_people(self,name='毛毛'):
#         print("我是超人，我会保护人民，我的名字叫：{}".format(name))
#
#     def fly_to_sky(self,name):
#         self.protect_people(name)
#         print("我是超人，我可以上天")
# person=SuperMan()
# person.protect_people("华华")
