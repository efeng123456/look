#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import time

from page.basepage import Page
from page.basetestcase import AppTestCase
import unittest
from page.loginPO import LoginPO

class testlogin(AppTestCase,LoginPO):

    def test_login(self):
        self.dologin()
        try:
            self.driver.find_element_by_id('com.minxing.chamc:id/title')
            print '登陆成功'
        except Exception as e:
            ##print e
            print '登陆失败'


if __name__=='__main()__':
    unittest.main

