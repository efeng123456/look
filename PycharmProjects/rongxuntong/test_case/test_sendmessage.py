#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import time

from page.basepage import Page
from page.basetestcase import AppTestCase
import unittest
from page.messagePO import messagePO
#from page.dialogPO2 import dialigPO
from page.talkPO import talkPO
import time

class testsengmessage(AppTestCase,messagePO,talkPO):

    def test_sendMessages(self):
        # self.menutapjob()
        # self.menutapmessage()
        self.choicetalk('message')
        time.sleep(2)

        self.message_content_et('test')
        self.send_click()
        self.send_status()



if __name__=='__main()__':
    unittest.main
