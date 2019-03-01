# _*_ coding:utf-8 _*_
from page.basepage import Page
##定义了消息界面各对象的定位和操作
class talkPO(Page):

    # search_permission=(id('com.android.packageinstaller:id/permission_allow_button'))
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
    ##发送按钮
    send='com.minxing.chamc:id/message_send_btn'
    ##添加内容暂时不做
    ##文件定位
    file_choice='com.minxing.chamc:id/file_click_area'
    ##预览
    file_preview="//android.widget.TextView[contains(@text,'预览')]"
    ##下载
    file_down="//android.widget.TextView[contains(@text,'下载')]"
    ##保存到网盘
    file_save="//android.widget.TextView[contains(@text,'保存到网盘')]"
    ##文件查看
    file_check="//android.widget.TextView[contains(@text,'查看')]"
    ##发送状态
    status='com.minxing.chamc:id/message_state'
    ##预览文件的imgxpath
    path_view="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.widget.Image"
    # def chick_permissino(self,search_permission):
    #     self.find_element(search_permission).chick()
    def balckClick(self):
        self.find_element('com.minxing.chamc:id/title_left_button').click()
    ##返回会话标题
    def titlename(self):
        print self.find_elementID('com.minxing.chamc:id/title_name').text
    ##进入会话详情
    def talkDetail(self):
        self.find_elementID('com.minxing.chamc:id/right_btn_check_person_detail').click()
    ##发送会话内容
    def message_content_et(self,message):
        self.find_elementID('com.minxing.chamc:id/message_content_et').send_keys(message)
    def send_click(self):
        self.find_elementID('com.minxing.chamc:id/message_send_btn').click()
    def send_status(self):
        try:
            self.find_elementID('com.minxing.chamc:id/message_state')
            print '发送失败'
        except Exception,e:
            print '发送成功'
    ##文件选择
    def file_choice(self):
        self.find_elementID('com.minxing.chamc:id/file_click_area').click()
    ##文件预览
    def file_preview(self):
        self.find_elementXpath("//android.widget.TextView[contains(@text,'预览')]").click()
    def file_down(self):
        self.find_elementXpath("//android.widget.TextView[contains(@text,'下载')]").click()
    def file_save(self):
        self.find_elementXpath("//android.widget.TextView[contains(@text,'保存到网盘')]").click()
    def file_check(self):
        self.find_elementXpath("//android.widget.TextView[contains(@text,'查看')]").click()
    def doc_view_status(self):
        try:
            self.find_elementXpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]/android.widget.Image")
            ##	/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[2]
            print '预览成功'
            return True
        except Exception as e:
            print '预览失败'
            self.get_screenSho()
            return False
    def doc_Api_status(self):
        try:
            self.find_elementID('listview')
            print '公文审批加载成功'
            return True
        except Exception as e:
            print '公文审批加载失败'
            self.get_screenSho()
            return  False

