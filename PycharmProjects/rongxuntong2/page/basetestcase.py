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