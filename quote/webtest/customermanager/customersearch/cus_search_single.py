import unittest

from quote.base.usebrowser import UseBrowser

from quote.util.operationexl import OperationExl
from quote.webpage.customermanager.searchpage import SearchPage
from quote.webpage.usermanager.loginpage import LoginPage


class CustomerSearch(unittest.TestCase):

    def setUp(self) -> None:
        self.loginpage = LoginPage()
        self.loginpage.login('admin', 'admin')
        self.sp = SearchPage()
        self.oe = OperationExl()

        # self.cp = CustomerPage()

    def test_1_search_all(self):
        self.sp.search()
        data=self.sp.get_data_first_page()
        print(data)
        expect_value = self.oe.get_cell_value(3,0).split(',')
        print(expect_value)
        self.assertEqual(expect_value,data)


        # self.cp.customer_add('c008')
        # actual_text = self.cp.customer_add_suc_text()
        # # print(actual_text)
        # self.assertEqual(actual_text,'添加记录成功！')

    def tearDown(self) -> None:
        UseBrowser.quit()


if __name__ == '__main__':
    unittest.main()
