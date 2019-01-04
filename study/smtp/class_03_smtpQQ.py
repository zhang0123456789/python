#！/usr/bin/env python
#_*_conding:dtf-8_*_
# @Time    : 2018/12/11 0011 下午 14:17
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : class_03_smtpQQ.py
'''直接邮箱密码登录，端口是25，ssl授权码端口是465或587'''
import smtplib
from email.mime.text import MIMEText

#----------1.跟发件相关的参数——————————————
smtpserver='smtp.qq.com'#发件服务器
port=465#端口
sender='1402686685@qq.com'#账号
psw='jthjwnndzyfabacd'#QQ授权码
receiver='m18576437695@163.com'#接收人


#——————————2.编辑邮件内容————————-——-
subject='这个是主题QQ'
body= '<p>这个是发送的QQ邮件</p>'     # 定义邮件正文为html格式
msg=MIMEText(body,'html','utf-8')
msg['from']=sender
msg['to']='m18576437695@163.com'
msg['subject']=subject


#----------------3.发送邮件——————————————
smtp=smtplib.SMTP()
smtp.connect(smtpserver)#连接服务器
smtp=smtplib.SMTP_SSL(smtpserver,port)
smtp.login(sender,psw)#登录
smtp.sendmail(sender,receiver,msg.as_string())#发送
smtp.quit()#关闭


