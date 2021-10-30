import HwTestReport
import time
import unittest

from quote.base.usebrowser import UseBrowser
from quote.util.operationexl import OperationExl
from quote.webpage.usermanager.loginpage import LoginPage
from quote.webtest.customermanager.customeradd.customeradd_suc import CustomerAddSuc
from quote.webtest.usermanager.login.loginfail import LoginFail


class LoginSuc(unittest.TestCase):

    def setUp(self) -> None:
        self.loginpage = LoginPage()
        self.oe = OperationExl()


    def test_1_login_suc(self):
        self.loginpage.login(self.oe.get_cell_value(1,2),self.oe.get_cell_value(1,3))
        actual_text = self.loginpage.get_suc_text()
        print(actual_text)
        self.assertEqual(self.oe.get_cell_value(1,4),actual_text)
        # time.sleep(3)

    # def test_2_login_suc(self):
    #     self.loginpage.login('2222','2222')
    #     time.sleep(3)
    #
    # def test_3_login_suc(self):
    #     self.loginpage.login('3333','3333')
    #     time.sleep(3)

    def tearDown(self) -> None:
        UseBrowser.quit()



if __name__ == '__main__':
    suite = unittest.TestSuite()
    # TestCaseOne  用例进行加载
    login_suc = unittest.TestLoader().loadTestsFromTestCase(LoginSuc)
    # TestCaseTwo 用例进行加载
    login_fail = unittest.TestLoader().loadTestsFromTestCase(LoginFail)
    # TestCaseTwo 用例进行加载
    customer_add_suc = unittest.TestLoader().loadTestsFromTestCase(CustomerAddSuc)
    # 所有的case放入列表
    all_case = [login_suc,login_fail,customer_add_suc]
    # 把case放入测试套件
    suite.addTests(all_case)
    # 运行对象runner
    # runner = unittest.TextTestRunner(verbosity=2)
    # # 执行测试套件
    # runner.run(suite)

    with open('../../../report/auto_report.html', 'wb+') as fp:
        runner=HwTestReport.HTMLTestReport(stream=fp,
            title='My auto test',
            description='This demonstrates the report output by HTMLTestRunner.',
            verbosity=2)
        runner.run(suite)