#!/usr/bin/env python 
# encoding: utf-8
# time: 2018/12/11 19:50
# author: 蜜蜜
# file: learn_smtpblib.py
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#--------跟发件相关的参数-----
smtpsever='smtp.163.com'
port=465
sender=''
