#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/11/18 9:30
'''1：创建一个名为 User 的类，其中包含属性 first_name 和 last_name，
还有用户简介通常会存储的其他几个属性。在类 User 中定义一个名为 describe_user()的方法，
它打印用户信息摘要；再定义一个名为 greet_user()的方法，它向用户发出个性化的问候。
 创建多个表示不同用户的实例，并对每个实例都调用上述两个方法。'''
'''对象方法调用对象方法'''
# class User:
#     def __init__(self,first_name,last_name,height,weight,age):  #初始化函数
#         self.first_name=first_name
#         self.last_name=last_name
#         self.height=height
#         self.weight=weight
#         self.age=age
#
#     def describe_user(self):  #对象方法
#         print(self.first_name+self.last_name+'的身高是'+self.height+'的体重是'+self.weight+'性别是'+self.age)
#         self.greet_user()
#
#     def greet_user(self):  #对象方法
#         print('hi,how are you')
#         print('you are so tall')
#         print('you are a  Handsome man')
#
# p1=User('yong','li','175','68','boy')   #初始化定义 创建对象就得传参数
# p2=User('qiang','zhang','191','80','boy')
# p3=User('gang','wang','184','75','boy')
# p1.describe_user()
# p2.describe_user()
# p3.describe_user()



'''对象方法里面调用静态方法'''
# class User:
#     def __init__(self,first_name,last_name,height,weight,age):  #初始化函数
#         self.first_name=first_name
#         self.last_name=last_name
#         self.height=height
#         self.weight=weight
#         self.age=age
#
#
#     def describe_user(cls,first_name,last_name,height,weight,age):
#         print(cls.first_name+cls.last_name+'的身高是'+cls.height+'的体重是'+cls.weight+'性别是'+cls.age)
#         cls.greet_user()
#     @staticmethod
#     def greet_user():
#         print('hi,how are you')
#         print('you are so tall')
#         print('you are a  Handsome man')
# p1=User('yong','li','175','68','boy')
# p1.describe_user('yong','li','175','68','boy')
# print("")
# p2=User('qiang','zhang','191','80','boy')
# p2.describe_user('qiang','zhang','191','80','boy')
# print("")
# p3=User('gang','wang','184','75','boy')
# p3.describe_user('gang','wang','184','75','boy')


'''2：定义一个学生类。
1）有下面的类属性： 1 姓名 2 年龄 3 成绩（语文，数学，英语)[每课成绩的类型为整数] ,
均放在初始化函数里面。
2）类方法：
a)获取学生的姓名：get_name() 返回类型:str b)获取学生的年龄：get_age() 返回类型:int
c) 返回3门科目中最高的分数。get_course() 返回类型:int
写好类以后，可以定义2个同学测试下: zm = Student('zhangming',20,[69,88,100]) 返回结果：
 zhangming 20 100'''

# class StudentInfo:
#     def __init__(self,name,age,grade):
#         self.name=name
#         self.age=age
#         self.grade=grade
#
#     def get_name(self):
#         return self.name
#     def get_age(self):
#         return self.age
#     def get_course(self):
#         return max(self.grade)
#
# p1=StudentInfo('zhangming','20',[69,88,100])
# print(p1.get_name())
# print(p1.get_age())
# print(p1.get_course())



'''3.人和机器猜拳游戏写成一个类，有如下几个函数：
1）函数1：选择角色1 曹操 2张飞 3 刘备
2）函数2：角色猜拳1剪刀 2石头 3布 玩家输入一个1-3的数字
3）函数3：电脑出拳 随机产生1个1-3的数字，提示电脑出拳结果
4）函数4：角色和机器出拳对战，对战结束后，最后出示本局对战结果...赢...输,
然后提示用户是否继续？按y继续，按n退出。
5）最后结束的时候输出结果 角色赢几局 电脑赢几局，平局几次 游戏结束'''

# import random
# class Game():
#     def __init__(self): #将胜负数作为类属性，方便在下面的方法中计算次数
#         self.win_num = 0
#         self.lose_num = 0
#         self.draw_num = 0
#     '''选择角色，并打印'''
#     def choose_player(self):
#         try:
#             self.role = int(input('there is threee players to choose: 曹操（1）、张飞（2）、刘备（3） '))
#         except ValueError:
#             print('please input a digit!')
#         else:
#             if self.role == 1:
#                 print('your role is: 曹操')
#             elif self.role == 2:
#                 print('your role is: 张飞')
#             elif self.role == 3:
#                 print('your role is: 刘备')
#             else:
#                 print('there is no player for you, try again!')
#
#
#     '''用户开始猜拳，并打印'''
#     def player_guessing(self):
#         try:
#             self.plyer_choice = int(input('which one will you guess: 剪刀（1）、石头（2）、布（3）'))
#         except ValueError:
#             print('please input a digit!')
#         else:
#             if self.plyer_choice == 1:
#                 print('your choice is: 剪刀')
#             elif self.plyer_choice == 2:
#                 print('your choice is: 石头')
#             elif self.plyer_choice == 3:
#                 print('your choice is: 布')
#             else:
#                 print('try again!')
#
#     '''随机产生1个1-3的数字，提示电脑出拳结果'''
#     def computer_guessing(self):
#         self.computer_choice = random.randint(1, 3)
#         if self.computer_choice==1:
#             print("computer's choice is: 剪刀")
#         elif self.computer_choice==2:
#             print("computer's choice is: 石头")
#         elif self.computer_choice==3:
#             print("computer's choice is: 布")
#
#     '''人机对战，判断胜平负'''
#     def pk(self):
#         if (self.plyer_choice==1 and self.computer_choice==3)or(self.plyer_choice==2 and self.computer_choice==1)or(self.plyer_choice==3 and self.computer_choice==2):
#             print('you win!')
#             self.win_num+=1 #以上几种胜利情况出现时，将表示胜利次数变量加1
#         elif self.plyer_choice==self.computer_choice:
#             print('draw')
#             self.draw_num+=1 # 平局时+1
#         elif self.plyer_choice>3:
#             print('input error! invaild!')
#         else:
#             print('you lose')
#             self.lose_num+=1 # 败北时记录+1
#
# guessing_gama=Game()
# guessing_gama.choose_player()
# while(1):
#     guessing_gama.player_guessing()
#     guessing_gama.computer_guessing()
#     guessing_gama.pk()
#     a = input(' enter "Y" to contiune, enter "N" to quit')
#     if a.lower() == 'n':
#         print('game over!')
#         break
#     else:
#         continue
# print('The game result:')
# print('win: ',guessing_gama.win_num)
# print('lose: ',guessing_gama.lose_num)
# print('draw: ',guessing_gama.draw_num)








'''4：按照以下要求定义一个游乐园门票类，并创建实例调用函数，
完成儿童和大人的总票价统计（人数不定，由你输入的人数个数来决定）
1)平日票价100元
2)周末票价为平日票价120%
3)儿童半价'''


'''对象方法'''
class ParkTickets:
    def _init_(self,adults,kids):
        self.adults=adults
        self.kids=kids
    def weekend(self):
        print("周末总票价:{}".format(120*self.adults+60*self.kids))
    def normal(self):
        print("平时总票价:{}".format(100* self.adults + 50 *self.kids))
p1=ParkTickets(10,3)
p1.weekend()
p1.normal()










