#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import smtplib
from email.mime.text import MIMEText
import unittest
import os
import time
from appium import webdriver
import ddt
import platform
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
# import warnings
#
# from Modu.ReadConfig import ReadConfig

class AppTestCase(unittest.TestCase):
    def setUp(self):
        # super().setUp()
        # 初始化设备对象
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = os.popen('adb shell getprop ro.build.version.release').read()
        desired_caps['deviceName'] = os.popen('adb devices').read().split('\n')[1].split('\t')[0]
        desired_caps['appPackage'] = 'com.minxing.chamc'
        # desired_caps['app'] = 'F:// debug.apk'
        ##设置是否每次重置应用
        desired_caps['noReset'] = 'True'
        desired_caps['appActivity'] = 'com.minxing.client.LoadingActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(10)
    def tearDown(self):
        self.driver.quit()




# class AppTestCase(unittest.TestCase,ReadConfig):
#
#     def setUp(self):
#         # warnings.simplefilter("ignore", ResourceWarning)
#         web_or_native = ReadConfig().get_android("web_or_native")
#         android_or_ios = ReadConfig().get_android("android_or_ios")
#         desired_caps={}
#         if web_or_native == 'native':
#             desired_caps['platformName'] = ReadConfig().get_android("platform_name")
#             desired_caps['platformVersion'] = ReadConfig().get_android("platform_version")
#
#         elif web_or_native == 'web':
#             desired_caps['browserName'] = ReadConfig().get_android("browser_name")
#
#         desired_caps['deviceName'] = ReadConfig().get_android("device_name")
#
#         if android_or_ios == 'android':
#             desired_caps['appPackage'] = ReadConfig().get_android("app_package")
#             desired_caps['appActivity'] = ReadConfig().get_android("app_activity")
#
#         elif android_or_ios == 'ios':
#             desired_caps['app'] = ReadConfig().get_android("app")
#             desired_caps['udid'] = ReadConfig().get_android("udid")
#
#         #输入中文
#         desired_caps['resetKeyboard'] = ReadConfig().get_android("reset_keyboard")
#         desired_caps['unicodeKeyboard'] = ReadConfig().get_android("unicode_keyboard")
#         desired_caps['newCommandTimeout'] = ReadConfig().get_android("new_command_timeout")
#         desired_caps['sessionOverride'] = ReadConfig().get_android("session_override")
#         # desired_caps['recreateChromeDriverSessions']=config.recreate_chrome_driver_sessions
#         desired_caps['noReset'] = ReadConfig().get_android("no_reset")
#         desired_caps['automationName'] = 'uiautomator2'  #1.6抓取toast专用
#         self.driver=webdriver.Remote(ReadConfig().get_android("web_server"),desired_caps)

