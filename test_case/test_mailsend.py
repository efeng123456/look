#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import time

from page.basepage import Page
from page.basetestcase import AppTestCase
import unittest
from page.messagePO import messagePO
from page.jobdeskPO import jobDeskPO
from page.mailPO import mailPO
#from page.dialogPO2 import dialigPO
from page.talkPO import talkPO
import time
from page.loginPO import LoginPO
class testmailSend(AppTestCase,messagePO,jobDeskPO,mailPO,LoginPO):

    def test_mailSend(self):
        self.loginStatus()
        self.menutapjob()
        time.sleep(2)
        self.choicjob('企业邮箱')
        time.sleep(5)
        self.readmail()
        time.sleep(2)
        self.sendmail2()
        self.send_mail_status()

if __name__=='__main()__':
    unittest.main
