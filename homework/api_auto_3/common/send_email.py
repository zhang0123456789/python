import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 
from email.mime.application import MIMEApplication

#邮件发送的用户名和密码  常识：第三方授权码
_user = "1255811581@qq.com"
_pwd = "请填写自己的授权码"

now = time.strftime('%Y-%m-%d_%H_%M_%S')#获取时间戳

class sendEmail:
    def send_email(self,email_to,path_list):
        #email_to  收件方
        #filepath 你要发送附件的地址
        #如名字所示Multipart就是分多个部分
        msg = MIMEMultipart()
        msg["Subject"] = now+"华华的测试报告"
        msg["From"]  = _user
        msg["To"]   = email_to

        #---这是文字部分---
        part = MIMEText("这次是自动化测试结果，请查收！")
        msg.attach(part)

        #---这是附件部分---
        for path in path_list:#path_list 路径列表
            part = MIMEApplication(open(path,'rb').read())
            part.add_header('Content-Disposition', 'attachment', filename='test_api.html')
        msg.attach(part)#附件跟正文一起发送
        s = smtplib.SMTP_SSL("smtp.qq.com", timeout=30)#连接smtp邮件服务器,端口默认是25
        s.login(_user, _pwd)#登陆服务器
        s.sendmail(_user, email_to, msg.as_string())#发送邮件
        s.close()

if __name__ == '__main__':
    sendEmail().send_email("775341320@qq.com",r"E:\2018Python课件&代码\code\python_10\API_Frame_Work_1019\test_result\report\test_api.html")
