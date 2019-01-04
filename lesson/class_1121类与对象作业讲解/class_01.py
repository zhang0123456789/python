#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/11/24 9:09
'''3.人和机器猜拳游戏写成一个类，有如下几个函数：
1）函数1：选择角色1 曹操 2张飞 3 刘备
2）函数2：角色猜拳1剪刀 2石头 3布 玩家输入一个1-3的数字
3）函数3：电脑出拳 随机产生1个1-3的数字，提示电脑出拳结果
4）函数4：角色和机器出拳对战，对战结束后，最后出示本局对战结果...赢...输,
然后提示用户是否继续？按y继续，按n退出。
5）最后结束的时候输出结果 角色赢几局 电脑赢几局，平局几次 游戏结束'''
# '''方法1'''
# class HumanVsPC:
#     def role(self):#选择角色
#         role_num=input("请根据数字选择角色：1 曹操 2张飞 3 刘备")
#         if role_num=='1':
#             role='曹操'
#         elif role_num=='2':
#             role = '张飞'
#         elif role_num=='3':
#             role = '刘备'
#         else:
#             role='输入的数字错误'
#         print("你选择的角色是：{}".format(role))
#
# if __name__=='__main__':
#     HumanVsPC().role()


'''方法2'''
# class HumanVsPC:
#     def role(self):#选择角色
#         role_dict={'1':'曹操','2':'张飞','3':'刘备'}
#         role_num = input("请根据数字选择角色：1 曹操 2张飞 3 刘备")
#         try:
#             role_name=role_dict[role_num]
#         except Exception as e:
#             print("输入的数字错误：",e,'默认选择的角色曹操')
#             role_name='曹操'
#         print("你选择的角色是{}".format(role_name))
# if __name__=='__main__':
#     HumanVsPC().role()

'''方法3'''
import  random
class HumanVsPC:
    def role(self):#选择角色
        role_dict={'1':'曹操','2':'张飞','3':'刘备'}
        role_num = input("请根据数字选择角色：1 曹操 2张飞 3 刘备")
        while role_num not in role_dict.keys():
            role_num = input("请根据数字选择角色：1 曹操 2张飞 3 刘备")
        print("你选择的角色是{}".format(role_dict[role_num]))
        return  role_dict[role_num]

    def human_fist(self): #角色出拳
        fist_dict = {'1': '剪刀', '2': '石头', '3': '布'}
        fist_num = input("请根据数字选择角色：1 剪刀 2石头3 布")
        while fist_num not in fist_dict.keys():
            fist_num = input("请根据数字选择角色：1 剪刀 2石头3 布")
        print("你去的拳是{}".format(fist_dict[fist_num]))
        return fist_num

    def pc_fist(self):#电脑出拳
        fist_dict = {'1': '剪刀', '2': '石头', '3': '布'}
        fist_num = random.randint(1,3)  #随机产生的数是int类型
        print("pc出拳：{}".format(fist_dict[str(fist_num)]))
        return fist_num

    def human_vs_pc(self): #对战
        role_name=self.role()#角色名
        a=0#统计角色赢的次数
        b=0#统计电脑赢的次数
        c=0#统计平局的 次数
        while True:
            human_fist=int(self.human_fist())#角色出拳
            pc_fist=self.pc_fist()#电脑出拳
            if human_fist-pc_fist==-2 or human_fist-pc_fist==1:
                print("{}赢了".format(role_name))
                a+=1
            elif pc_fist-human_fist in (1,-2):
                print("电脑赢了")
                b+=1
            else:
                print("平局")
                c+=1
            choice=input("是否要继续出拳，y:继续，任意键:退出")
            if choice=='y':
                continue
            else:
                break
        print("本次对战，{}赢了{}次，电脑赢了{}次，平局了{}次".format(role_name,a,b,c))

#{'1': '剪刀', '2': '石头', '3': '布'}
#human:1 2 3
#   pc:3 1 2
''' human-pc  赢 -2 1'''
#   pc:1 2 3
#human:3 1 2
'''pc-human pc赢 -2 1'''


if __name__=='__main__':
    HumanVsPC().human_vs_pc()

