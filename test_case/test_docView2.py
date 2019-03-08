#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import time
#from appium import webdriver
from page.basepage import Page
from page.basetestcase import AppTestCase
import unittest
from page.messagePO import messagePO
#from page.dialogPO2 import dialigPO
from page.talkPO import talkPO
from page.loginPO import LoginPO
import time
class docview(AppTestCase,messagePO,talkPO,LoginPO):


    def test_docViews(self):
        # self.menutapjob()
        # self.menutapmessage()
        self.loginStatus()
        self.choicetalk('文件预览')
        time.sleep(5)
        self.file_choice()

        self.file_preview()
        time.sleep(5)
        #self.up()
        self.doc_view_status()
        # self.getScreenShot()
        time.sleep(5)
        if self.doc_view_status():
            print ''

        else:
            self.get_screenShort()
            print '执行失败'
        time.sleep(5)

if __name__=='__main()__':
    unittest.main
