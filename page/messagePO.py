# _*_ coding:utf-8 _*_
from page.basepage import Page
##定义了消息界面各对象的定位和操作
class messagePO(Page):

    # search_permission=(id('com.android.packageinstaller:id/permission_allow_button'))
    ##"消息"
    title = 'com.minxing.chamc:id/title'
    ##"查询"
    search = "com.minxing.chamc:id/title_right_search_function"
    ##"新建"
    new = 'com.minxing.chamc:id/title_right_new_function'
    menutapmessage="//android.widget.TextView[contains(@text,'消息')]"
    menutapjob="//android.widget.TextView[contains(@text,'工作')]"
    menutapaddress="//android.widget.TextView[contains(@text,'通讯录')]"
    menutapmy="//android.widget.TextView[contains(@text,'我')]"

    # def chick_permissino(self,search_permission):
    #     self.find_element(search_permission).chick()
    ##切换至消息
    def menutapmessage(self):
        self.find_elementXpath("//android.widget.TextView[contains(@text,'消息')]").click()
    ##切换至通讯录
    def menutapjob(self):
        self.find_elementXpath("//android.widget.TextView[contains(@text,'工作')]").click()
    ##切换至工作
    def menutapaddress(self):
      self.find_elementXpath("//android.widget.TextView[contains(@text,'通讯录')]").click()
    ##切换至我
    def menutapmy(self):
        self.find_elementXpath("//android.widget.TextView[contains(@text,'我')]").click()
    def choicetalk(self,talkname):
       # path="//android.widget.TextView[contains(@text,'talk')]"
        path = "//android.widget.TextView[contains(@text,'"+talkname+"')]"
        self.find_elementXpath(path).click()
       # print path



