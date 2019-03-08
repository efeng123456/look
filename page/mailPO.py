# _*_ coding:utf-8 _*_
from page.basepage import Page
class mailPO(Page):
    ##定义几个按钮
    ##邮件菜单
    mail_message_list_menu='com.minxing.chamc:id/btn_mx_mail_message_list_menu'
    ##写邮件
    ##退出邮件
    mail_message_list_exit='com.minxing.chamc:id/btn_mx_mail_message_list_exit'
    ##邮件操作
    mailmenuxpth="//android.widget.TextView[contains(@text,'全部已读')]"
    ##收件地址
    contact_btn_container='com.minxing.chamc:id/contact_btn_container'
    ##发件主题
    mailSubject='com.minxing.chamc:id/subject'
    ##发件内容
    message_content='com.minxing.chamc:id/message_content'
    ##发送按钮
    message_compose_send='com.minxing.chamc:id/tv_mx_mail_message_compose_send'
    ##未读状态
    subject_unread_flag='com.minxing.chamc:id/subject_unread_flag'
    def readmail(self):
        self.find_elementXpath("//android.widget.TextView[contains(@text,'全部已读')]").click()
    def mailaddress(self,address):
        self.find_elementID('com.minxing.chamc:id/contact_btn_container').send_keys(address)
    def mailSubject(self,subject):
        self.find_elementID('com.minxing.chamc:id/subject').send_keys(subject)
    def message_conten(self,Content):
        self.find_elementID('com.minxing.chamc:id/message_content').send_keys()
    def message_compose_send(self):
        self.find_elementID('com.minxing.chamc:id/tv_mx_mail_message_compose_send').click()
    def send_mail_status(self):
        try:
            self.find_elementID('com.minxing.chamc:id/subject_unread_flag')
            print '发送成功'
            return True
        except Exception as e:
            print e
            return False
    def sendmail2(self):
        a = self.getconf()[2]
        self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'写邮件')]").click()
        self.sleeps(3)
        self.driver.find_element_by_id('com.minxing.chamc:id/contact_btn_container').send_keys(a)
        self.sleeps(3)
        self.driver.find_element_by_id('com.minxing.chamc:id/subject').send_keys('test')
        self.sleeps(3)
        self.driver.find_element_by_id('com.minxing.chamc:id/message_content').send_keys('testmail')
        self.sleeps(3)
        self.driver.find_element_by_id('com.minxing.chamc:id/tv_mx_mail_message_compose_send').click()
        self.sleeps(3)
    def sendmaile(self):
        a = self.getconf()[2]
        self.mailaddress(a)
        self.mailSubject('testSendmail')
        self.message_conten('这是一个测试邮件')
        self.message_compose_send()


