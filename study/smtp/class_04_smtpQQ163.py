#！/usr/bin/env python
#_*_conding:dtf-8_*_
# @Time    : 2018/12/15 0015 上午 10:53
# @Author  : 蜜蜜
# @Email   : 1402686685@qq.com
# @File    : class_04_smtpQQ163.py
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#---------1.跟发件相关的参数-----------
smtpserver='smtp.163.com'#发件服务器
port=465                 #端口
sender='m18576437695@163.com'
psw='zhang199217'        #密码
# receiver = ["xxxx@qq.com"]      # 单个接收人也可以是list
receiver = ["2177758688@qq.com", "1402686685@qq.com"]   # 多个收件人list对象

#--------2.编辑内容----------
'''读文件'''
file_path='test_api12.html'
with open(file_path,'rb') as fp:
    mail_body=fp.read()
msg=MIMEMultipart()
msg['from']=sender
msg['to']=";".join(receiver)
msg['subject']='这是我的主题9999999'

'''正文'''
body=MIMEText(mail_body,'html','utf-8')
msg.attach(body)
'''附件'''
att=MIMEText(mail_body,'base64','utf-8')
att['Content-Type']='application/octet-stream'
att['Content-Disposition']='attachment;filename="test_report.html"'
msg.attach(att)

#---------------3.发送邮件——————————————
try:
    smtp=smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(sender,psw)
except:
    smtp=smtplib.SMTP_SSL(smtpserver,port)
    smtp.login(sender,psw)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()