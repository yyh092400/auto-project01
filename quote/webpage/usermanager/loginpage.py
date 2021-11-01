
from quote.base.operationbrowser import OperationBrowser
from quote.base.usebrowser import UseBrowser
from quote.util.loginfo import AutoLog
from quote.util.operationexl import OperationExl
from quote.util.operationyaml import OperationYaml


class LoginPage:

    def __init__(self):
        self.ub = UseBrowser('chrome', '../../../chromedriver.exe')
        self.ob = OperationBrowser(UseBrowser.driver)
        self.eo = OperationExl()
        self.oy = OperationYaml('../../../config/locator.yaml')
        self.logger = AutoLog()

    #登录功能
    def login(self,username='',password=''):
        self.logger.set_info('info','打开网址:'+self.eo.get_cell_value(1,1))
        self.ob.open_url(self.eo.get_cell_value(1,1))
        self.logger.set_info('info','输入用户名:'+username)
        self.ob.input_text('name',self.oy.get_locator('LoginPage','username'),username)
        self.logger.set_info('info', '输入密码:' + password)
        self.ob.input_text('name',self.oy.get_locator('LoginPage','password'),password)
        self.logger.set_info('info', '提交')
        self.ob.click('name',self.oy.get_locator('LoginPage','submit'))

    #获取登录成功页面的文本信息
    def get_suc_text(self):
        self.ob.change_frame(self.oy.get_locator('LoginPage','framemain'))
        return self.ob.get_text_xpath(self.oy.get_locator('LoginPage','sucinfo'))


    #获取失败信息文本
    def get_fail_text(self):
        return self.ob.get_text_xpath(self.oy.get_locator('LoginPage','failinfo'))
