#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from appium import webdriver
import time
from page.basepage import Page
from page.basetestcase import AppTestCase
import unittest
from page.messagePO import messagePO
from page.jobdeskPO import jobDeskPO
from page.talkPO import talkPO
import time

class testdocApi(AppTestCase,messagePO,jobDeskPO,talkPO):

    def test_docApi(self):

        self.menutapjob()
        time.sleep(2)
        self.choicjob('公文审批')
        time.sleep(15)
        self.doc_Api_status()
        self.mailtest()

if __name__=='__main()__':
    unittest.main
