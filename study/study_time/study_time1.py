#!/usr/bin/env python
# -*- coding:utf-8-*-
#@author:蜜蜜
#@file: study_time1.py 
#@time: 2018/12/28 
#@email:1402686685@qq.com

import time
'''#常用方法
1.time.sleep(secs)                (线程)推迟指定的时间运行。单位为秒。
2.time.time()                       获取当前时间戳'''

'''在Python中，通常有这三种方式来表示时间：时间戳、元组(struct_time)、格式化的时间字符串：
(1)时间戳(timestamp) ：通常来说，时间戳表示的是从1970年1月1日00:00:00开始按秒计算的偏移量。我们运行“type(time.time())”，返回的是float类型。
(2)格式化的时间字符串(Format String)： ‘1999-12-06’
(3)元组(struct_time) ：struct_time元组共有9个元素共九个元素:(年，月，日，时，分，秒，一年中第几周，一年中第几天等）'''

#打印时间戳
# import time
# print(time.time())
'''%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身'''
#时间字符串
import  time
# print(time.strftime("%Y-%m-%d  %X"))#打印本地相应的时间           2018-12-28  20:14:46
# print(time.strftime("%Y-%m-%d  %x"))#打印本地相应的日期           2018-12-28  12/28/18
# print(time.strftime("%Y-%m-%d  %W"))#打印一年中的星期数（00-53）星期一为星期的开始   2018-12-28  52
# print(time.strftime("%Y-%m-%d  %U"))#打印一年中的星期数（00-53）星期天为星期的开始   2018-12-28  51
# print(time.strftime("%Y-%m-%d  %y"))  # 打印两位数的年份表示（00-99）   2018-12-28  18
# print(time.strftime("%Y-%m-%d  %Y"))#打印四位数的年份表示（000-9999）   2018-12-28  2018
# print(time.strftime("%Y-%m-%d  %m"))#打印月份（01-12）2018-12-28  12
# print(time.strftime("%Y-%m-%d  %a"))#打印本地简化星期名称   2018-12-28  Fri
# print(time.strftime("%Y-%m-%d  %A"))#打印本地完整星期名称   2018-12-28  Friday
# print(time.strftime("%Y-%m-%d  %b"))#打印本地简化的月份名称  2018-12-28  Dec
# print(time.strftime("%Y-%m-%d  %B"))#打印本地完整的月份名称  2018-12-28  December
# print(time.strftime("%Y-%m-%d  %c"))#本地相应的日期表示和时间表示  2018-12-28  Fri Dec 28 20:21:35 2018

'''时间元组:localtime将一个时间戳转换为当前时区的struct_time'''
# import time
# print(time.localtime())
#打印出  time.struct_time(tm_year=2018, tm_mon=12, tm_mday=28, tm_hour=20, tm_min=24, tm_sec=5, tm_wday=4, tm_yday=362, tm_isdst=0)

'''时间戳-->结构化时间'''
# print(time.gmtime(1500000000))#打印time.struct_time(tm_year=2017, tm_mon=7, tm_mday=14, tm_hour=2, tm_min=40, tm_sec=0, tm_wday=4, tm_yday=195, tm_isdst=0)
# print(time.localtime(1500000000))#打印time.struct_time(tm_year=2017, tm_mon=7, tm_mday=14, tm_hour=2, tm_min=40, tm_sec=0, tm_wday=4, tm_yday=195, tm_isdst=0)

'''结构化时间-->时间戳　,  time.mktime(结构化时间)'''
# time_tuple=time.localtime(1500000000)
# print(time.mktime(time_tuple))


'''#时间戳 --> %a %b %d %H:%M:%S %Y串
#time.ctime(时间戳)  如果不传参数，直接返回当前时间的格式化串'''
# print(time.ctime())                  #打印：Fri Dec 28 20:33:06 2018
# print(time.ctime(1500000000))        #打印：Fri Jul 14 10:40:00 2017

'''
#结构化时间 --> %a %b %d %H:%M:%S %Y串
#time.asctime(结构化时间) 如果不传参数，直接返回当前时间的格式化串'''
# print(time.asctime(time.localtime(1500000000))) #打印：Fri Jul 14 10:40:00 2017
# print(time.asctime())#打印：Fri Dec 28 20:36:37 2018

'''计算时间差'''
true_time=time.mktime(time.strptime('2017-09-11 08:30:00','%Y-%m-%d %H:%M:%S'))
time_now=time.mktime(time.strptime('2017-09-12 11:00:00','%Y-%m-%d %H:%M:%S'))
dif_time=time_now-true_time
print(dif_time)
struct_time=time.gmtime(dif_time)
print('过去了%d年%d月%d天%d小时%d分钟%d秒'%(struct_time.tm_year-1970,struct_time.tm_mon-1,
                                       struct_time.tm_mday-1,struct_time.tm_hour,
                                       struct_time.tm_min,struct_time.tm_sec))
