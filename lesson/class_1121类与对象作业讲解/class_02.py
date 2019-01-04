#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/11/24 11:36
'''4：按照以下要求定义一个游乐园门票类，并创建实例调用函数，
完成儿童和大人的总票价统计（人数不定，由你输入的人数个数来决定）
1)平日票价100元
2)周末票价为平日票价120%
3)儿童半价'''
# class Ticket:
#     def count_ticket(self):#统计总票价
#         normal_price=100
#         weekend_price=120
#         adult_num=2
#         child_num=1
#         day_num=input("请输入你哪天去游乐园：1-7分别代表周一到周天")
#         if day_num in ('1','2','3','4','5'):
#             child_price=normal_price*0.5
#             total=adult_num*100+child_num*child_price
#         else :
#             child_price=weekend_price*0.5
#             total=adult_num*weekend_price+child_price*child_num
#         print("大人：{},小孩{}，总价格是{}".format(adult_num,child_num,total))
# if __name__=='__main__':
#     Ticket().count_ticket()

class Ticket:
    @staticmethod
    def count_ticket(normal_price=100,weekend_price=120):#统计总票价
        adult_num=int(input("请输入大人的人数"))
        child_num=int(input("请输入小孩的人数"))
        day_num=input("请输入你哪天去游乐园：1-7分别代表周一到周天")
        if day_num in ('1','2','3','4','5'):
            child_price=normal_price*0.5
            total=adult_num*100+child_num*child_price
        else :
            child_price=weekend_price*0.5
            total=adult_num*weekend_price+child_price*child_num
        print("大人：{},小孩{}，总价格是{}".format(adult_num,child_num,total))
if __name__=='__main__':
    Ticket().count_ticket()