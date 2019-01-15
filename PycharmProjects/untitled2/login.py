#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import unittest
import os
import time
from appium import webdriver
import HTMLTestRunner

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
    ##登录
    # def test_login(self):
    #     print('test_login  ')
    #     driver=self.driver
    #     time.sleep(5)
    #     driver.find_element_by_id('com.minxing.chamc:id/username').send_keys('nametest')
    #     time.sleep(5)
    #     driver.find_element_by_id('com.minxing.chamc:id/password').send_keys('chamc@2019')
    #     time.sleep(5)
    #     driver.find_element_by_id('com.minxing.chamc:id/login_btn').click()
    #     time.sleep(5)
    #     try:
    #         driver.find_element_by_id('com.minxing.chamc:id/title_right_new_function')
    #         print '登陆成功'
    #     except Exception as e:
    #         ##print e
    #         print '登陆失败'
    #         ##这里后期调用异常操作处理程序做异常处理
    ##发送消息
    # def test_sendMassage(self):
    #     driver=self.driver
    #     # massage_list=driver.find_elements_by_id('com.minxing.chamc:id/conversation_avatar')
    #     #
    #     time.sleep(10)
    #     driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'没文化，哪有卖脑子的')]").click()
    #
    #     time.sleep(10)
    #     driver.find_element_by_id('com.minxing.chamc:id/message_content_et').send_keys('test send massage')
    #     time.sleep(5)
    #     driver.find_element_by_id('com.minxing.chamc:id/message_send_btn').click()
    #     time.sleep(10)
    #     try:
    #         driver.find_element_by_id('com.minxing.chamc:id/message_state')
    #     except Exception as e:
    #         print '发送成功'
    #     else:
    #         print  '发送失败'
    # 从网盘发送文件
    # def test_senddoc(self):
    #     driver = self.driver
    #     time.sleep(5)
    #     driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'没文化，哪有卖脑子的')]").click()
    #     time.sleep(5)
    #     driver.find_element_by_id('com.minxing.chamc:id/message_attach_btn').click()
    #     time.sleep(5)
    #     # 左划
    #     x = driver.get_window_size()['width']
    #     y = driver.get_window_size()['height']
    #     driver.swipe(x*3/4, y*0.8, x/4, y*0.8)
    #     time.sleep(5)
    #     # 从网盘选择文件进行发送
    #     driver.find_elements_by_id('com.minxing.chamc:id/app_grid_item_icon_mask')[0].click()
    #     driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'云盘迁移实施方案.docx')]").click()
    #     driver.find_element_by_id('com.minxing.chamc:id/dialog_ok').click()
    #     time.sleep(5)
    ##文件预览
    # def test_doc_view(self):
    #     driver=self.driver
    #     time.sleep(5)
    #     driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'文件预览')]").click()
    #     time.sleep(5)
    #     driver.find_element_by_id('com.minxing.chamc:id/file_click_area').click()
    #     time.sleep(3)
    #     driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'预览')]").click()
    #     time.sleep(3)
    #     x = driver.get_window_size()['width']
    #     y = driver.get_window_size()['height']
    #     driver.swipe(x*0.5, y*0.8, 0.5, y*0.2)
    #     time.sleep(1)
    #     try:
    #         driver.find_element_by_id('p2')
    #         print '预览成功'
    #     except:
    #         print '预览失败'
    #
    #     # def test_yonghuexit(self):
    #     #    driver=self.driver
    #     #    time.sleep(5)
    #     #    driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'我')]").click()
    #     #    time.sleep(5)
    #     #    driver.find_element_by_id('com.minxing.chamc:id/setting_text').click()
    #     #    time.sleep(5)
    #     #    driver.find_element_by_id('com.minxing.chamc:id/exit_btn').click()
    #     #    time.sleep(5)
    #     #    driver.find_element_by_id('com.minxing.chamc:id/dialog_ok').click()
    #     #    time.sleep(5)
    #     #    try:
    #     #        driver.find_element_by_id('com.minxing.chamc:id/username')
    #     #    except Exception as e:
    #     #        print '退出失败'
    #     #    else:
    #     #        print '退出成功'

    # def menu_tap(self,menu_value):
    #     driver = self.driver
    #     menu_value = menu_value
    #     xpath = "//android.widget.TextView[contains(@text,"+"'"+menu_value+"'"+")]"
    #     driver.find_element_by_xpath(xpath).click()
    #
    # menu_tap('我的')






    def test_workBenchmail(self):
        driver=self.driver
        time.sleep(5)
        driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'工作')]").click()
        time.sleep(5)
        driver.find_elements_by_id('com.minxing.chamc:id/app_avatar_iv')[0].click()
        time.sleep(5)










    # def test_workBenchDropbox(self):
    #     driver = self.driver
    #     time.sleep(5)
    #     driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'工作')]").click()
    #     time.sleep(5)
    #     driver.find_elements_by_id('com.minxing.chamc:id/app_avatar_iv')[1].click()
    #     time.sleep(2)
    # def test_workBenchDocument(self):
    #     driver = self.driver
    #     time.sleep(5)
    #     driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'工作')]").click()
    #     time.sleep(5)
    #     driver.find_elements_by_id('com.minxing.chamc:id/app_avatar_iv')[3].click()
    #     time.sleep(2)

    def tearDown(self):
        time.sleep(5)
        driver=self.driver

        print('tearDown ------ ')
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
