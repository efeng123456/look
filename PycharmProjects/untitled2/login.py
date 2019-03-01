#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import unittest
import os
import time
from appium import webdriver
import HTMLTestRunner
import pytest

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUp(self):
        # super().setUp()

        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8.0.0'
        desired_caps['deviceName'] = 'GWY0217817001150'
        desired_caps['appPackage'] = 'com.minxing.chamc'
        # desired_caps['app'] = 'F:// debug.apk'
        desired_caps['noReset'] = 'true'
        desired_caps['appActivity'] = 'com.minxing.client.LoadingActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    #登录
    def test_login(self):
        print('test_login  ')
        driver=self.driver
        time.sleep(5)
        driver.find_element_by_id('com.minxing.chamc:id/username').send_keys('nametest')
        time.sleep(5)
        driver.find_element_by_id('com.minxing.chamc:id/password').send_keys('chamc@2019')
        time.sleep(5)
        driver.find_element_by_id('com.minxing.chamc:id/login_btn').click()
        time.sleep(5)
        try:
            driver.find_element_by_id('com.minxing.chamc:id/title_right_new_function')
            print '登陆成功'
        except Exception as e:
            ##print e
            print '登陆失败'
            ##这里后期调用异常操作处理程序做异常处理
    #发送消息
    def test_sendMassage(self):
        driver=self.driver
        # massage_list=driver.find_elements_by_id('com.minxing.chamc:id/conversation_avatar')
        #
        time.sleep(10)
        driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'没文化，哪有卖脑子的')]").click()

        time.sleep(10)
        driver.find_element_by_id('com.minxing.chamc:id/message_content_et').send_keys('test send massage')
        time.sleep(5)
        driver.find_element_by_id('com.minxing.chamc:id/message_send_btn').click()
        time.sleep(10)
        try:
            driver.find_element_by_id('com.minxing.chamc:id/message_state')
        except Exception as e:
            print '发送成功'
        else:
            print  '发送失败'
##预览文件
    def test_docView(self):
        driver=self.driver
        time.sleep(10)
        driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'文件预览')]").click()
        time.sleep(5)
        driver.find_element_by_id('com.minxing.chamc:id/file_click_area').click()
        time.sleep(5)
        driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'预览')]").click()
        time.sleep(5)














    def tearDown(self):
        time.sleep(5)
        driver=self.driver

        print('tearDown ------ ')
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
