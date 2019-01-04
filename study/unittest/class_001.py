#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Time :2018/11/24 17:56
class Practice():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def Method(self):
        return self.a+self.b
if __name__=='__main__':
    a=Practice(5,1)
    print(a.Method())
