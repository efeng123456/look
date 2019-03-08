from page.basepage import Page
class LoginPO(Page):

    # search_permission=(id('com.android.packageinstaller:id/permission_allow_button'))
    usernameid = 'com.minxing.chamc:id/username'
    passwordid = "com.minxing.chamc:id/"
    loginid = 'com.minxing.chamc:id/login_btn'
    login_status='com.minxing.chamc:id/title'

    # def chick_permissino(self,search_permission):
    #     self.find_element(search_permission).chick()

    def input_username(self):
        self.find_elementID('com.minxing.chamc:id/username').send_keys('mobiletest')
    def input_password(self):
        self.find_elementID("com.minxing.chamc:id/password").send_keys('yongyou@2018')
    def checklogin(self):
        self.find_elementID('com.minxing.chamc:id/login_btn').click()
    def dologin(self):
        self.input_username()
        self.input_password()
        self.checklogin()
    def loginStatus(self):
        try:
            self.driver.find_element_by_id('com.minxing.chamc:id/title')
        except:
            self.dologin()
