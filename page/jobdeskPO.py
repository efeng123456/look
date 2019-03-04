# _*_ coding:utf-8 _*_
from page.basepage import Page
##定义了消息界面各对象的定位和操作
class jobDeskPO(Page):
##企业邮箱"//android.widget.TextView[contains(@text,'公文审批')]"
##企业网盘
##公文审批

    ##切换
    def choicjob(self,jobs):
        path = "//android.widget.TextView[contains(@text,'"+jobs+"')]"
        self.find_elementXpath(path).click()
        print path
    def docApi_status(self):
        pass



