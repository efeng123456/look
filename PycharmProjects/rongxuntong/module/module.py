# _*_ coding:utf-8 _*_
import smtplib
from email.mime.text import MIMEText
class Module():
    def mailtest(self):
        with open('./mailcontent.txt','a+') as f:
            print(f.read())
            f.write('111')


    def readfile(self):
        f = open("/Users/fengerqiang/Documents/问卷调查系统相关文档/test.txt","r")
        rows = []
        for eachline in f:
            tmp=[]
            tmp.append(eachline.split(','))
            rows.append(tmp)
            return rows

    def sendmail(msgvalue):
        #smtp服务器
        smtp_server = 'smtp.sina.com'
        receiver = 'efengsin@sina.com'
        msg=MIMEText(msgvalue,'plain','utf-8')
        #发送邮箱地址
        msg['From'] = 'efengsin@sina.com'
        #主题
        msg['Subject'] = 'from 融讯通测试'
        #收件箱地址
        msg['To'] = receiver
        server = smtplib.SMTP(smtp_server,25)
        server.login('efengsin@sina.com','0816211')
        server.sendmail('efengsin@sina.com',receiver,msg.as_string())
        server.quit()


