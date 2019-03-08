#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

sender = 'efengsin@sina.com'
receivers = ['efengsin@sina.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
def sendmails(filename):
    #创建一个带附件的实例
    message = MIMEMultipart()
    message['From'] = Header('efengsin@sina.com')
    message['To'] =  Header("ceshi")
    subject = 'testreeport'
    message['Subject'] = Header(subject)

    #邮件正文内容
    message.attach(MIMEText('test'))
    #
    # # 构造附件1，传送当前目录下的 test.txt 文件
    att1 = MIMEText(open(filename, 'rb').read())
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = 'attachment; filename="TestReport2019-03-07 20_42_08.html"'
    message.attach(att1)


    try:
        smtpObj = smtplib.SMTP('smtp.sina.com',25)
        smtpObj.login('efengsin@sina.com','0816211')
        smtpObj.sendmail(sender, receivers, message.as_string())
        print "邮件发送成功"
    except smtplib.SMTPException,e:
        print e
        print "Error: 无法发送邮件"


