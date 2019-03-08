# _*_ coding:utf-8 _*_

from appium import webdriver
from selenium.webdriver.support.expected_conditions import NoSuchElementException
#from selenium.webdriver.common.by import By
import time
import json
import platform
#from selenium.webdriver.support.ui import WebDriverWait
##基本的定位方法

class Page(object):
    driver =None
    def __init__(self,driver):
        self.driver = driver
    def find_element(self,*loc):
        try:
            return self.driver.find_element(*loc)
            t.sleep(5)
        except (NoSuchElementException,KeyError,ValueError,Exception),e:
            print 'Error details : %s'%(e.args[0])
    # find = find_element(By.ID,"com.minxing.chamc:id/username")

    def find_elementID(self,id):
        try:
            return self.driver.find_element_by_id(id)
        except(NoSuchElementException,KeyError,ValueError,Exception),e:
            print 'Error details : %s'%(e.args[0])
    def find_elementXpath(self,xpath):
        try:
            return self.driver.find_element_by_xpath(xpath)
        except(NoSuchElementException,KeyError,ValueError,Exception),e:
            print 'Error details : %s'%(e.args[0])
    # def get_screenshot(self):
    #     timestr=time.strftime('%Y.%m.%d',time.localtime(time.time()))
    #     self.driver.save_screenshot(timestr+'.png')
    # def getTime(self):
    #
    #     tamp = str(time.time())
    #
    #     return tamp
    ##装饰器样板，将根据装饰器修改
    # def makeBold(fun):
    #     print('----a----')
    #     def inner():
    #         print('----1----')
    #         return '<b>' + fun() + '</b>'
    #         return inner


    def get_screenShort(self):

        timestr=time.strftime('%Y.%m.%d',time.localtime(time.time()))
        filename = './errorimg/ %s.png' %timestr
        self.driver.get_screenshot_as_file(filename)

    def sleeps(self,Seconds):
        time.sleep(Seconds)
    def getWindow_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x,y
    def up(self):
        x = self.getWindow_size()[0]
        y = self.getWindow_size()[0]
        self.driver.swipe(x*0.5, y*0.9, x*0.5, y*0.1,2000)
    def down(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(x*0.5, y*0.1, x*0.5, y*0.9,200)
    def left(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(x*0.9, y*0.5, x*0.1, y*0.5,200)
    def right(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        self.driver.swipe(x*0.1, y*0.5, x*0.9, y*0.5,200)
    def mailappend(self,mailappend):
        self.mailtest(mailappend)
    def getconf(sefl):
        with open("..//conf/config.json",'r') as load_f:
            load_dict = json.load(load_f)
            # print(load_dict)["username"]
            return load_dict["username"],load_dict["password"],load_dict["mailaddress"]
