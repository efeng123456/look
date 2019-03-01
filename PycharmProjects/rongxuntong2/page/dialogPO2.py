# _*_ coding:utf-8 _*_
from page.basepage import Page
##会话页面，定位消息界面的元素及操作方法

class dialigPO(Page):
    ##black返回
    balck = 'com.minxing.chamc:id/title_left_button'
    ##会话标题
    titlename='com.minxing.chamc:id/title_name'
    ##会话详情
    talkDetail='com.minxing.chamc:id/right_btn_check_person_detail'
    ##语音按钮
    songButten='com.minxing.chamc:id/message_mode_switch_btn'
    ##内容输入框
    message_content_et='com.minxing.chamc:id/message_content_et'
    ##表情按钮
    message_smile='com.minxing.chamc:id/message_smile_btn'
    ##添加内容暂时不做
    ##点击返回按钮
    def balckClick(self):
        self.find_element('com.minxing.chamc:id/title_left_button').click()
    ##返回会话标题
    def titlename(self):
        print self.find_element('com.minxing.chamc:id/title_name').text
    ##进入会话详情
    def talkDetail(self):
        self.find_element('com.minxing.chamc:id/right_btn_check_person_detail').click()
    ##发送会话内容
    def message_content_et(self):
        self.find_element('com.minxing.chamc:id/message_content_et').send_keys('send message')
        print '我要执行'
