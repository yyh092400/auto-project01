import unittest

from quote.base.usebrowser import UseBrowser
from quote.util.operationexl import OperationExl
from quote.webpage.usermanager.loginpage import LoginPage

from ddt import ddt, data, unpack, file_data


@ddt
class LoginFail(unittest.TestCase):

    @classmethod
    def setUpClass(self) -> None:
        self.loginpage = LoginPage()
        self.oe = OperationExl()

    # @data([1,'admin','123456'],[2,'','123456'],[3,'admin',''])
    # @unpack
    # @file_data('../../../casedata/login/login.yaml')
    # def test_case(self,**kwargs):
    #     # if  kwargs['case_id']==1:
    #     #     self.loginpage.login(kwargs['username'], kwargs['password'])
    #     # elif kwargs['case_id']==2:
    #     #     self.loginpage.login(kwargs['username'], kwargs['password'])
    #     # elif kwargs['case_id']==3:
    #     self.loginpage.login(kwargs['username'], kwargs['password'])
    #     actual_text = self.loginpage.get_fail_text()
    #     self.assertEqual(actual_text, "请勿非法登录！")

    # def test_1_login_fail(self):
    #     self.loginpage.login()
    #     actual_text = self.loginpage.get_fail_text()
    #     self.assertEqual(actual_text,"请勿非法登录！")
    #
    def test_2_login_fail(self):
        self.loginpage.login(self.oe.get_cell_value(2,2),self.oe.get_cell_value(2,3))
        actual_text = self.loginpage.get_fail_text()
        self.assertEqual(actual_text,self.oe.get_cell_value(2,5))
    #
    # def test_3_login_fail(self):
    #     self.loginpage.login('','123456')
    #     actual_text = self.loginpage.get_fail_text()
    #     self.assertEqual(actual_text, "请勿非法登录！")
    #
    # def test_3_login_fail(self):
    #     self.loginpage.login('', '123456')
    #     actual_text = self.loginpage.get_fail_text()
    #     self.assertEqual(actual_text, "请勿非法登录！")

    @classmethod
    def tearDownClass(self) -> None:
        UseBrowser.quit()


if __name__ == '__main__':
    unittest.main()
