import unittest

from quote.base.usebrowser import UseBrowser
from quote.db.customermanager.customerdb import DbCustomer
from quote.webpage.customermanager.customerpage import CustomerPage
from quote.webpage.customermanager.searchpage import SearchPage
from quote.webpage.usermanager.loginpage import LoginPage


class CustomerAddSuc(unittest.TestCase):

    def setUp(self) -> None:
        self.loginpage = LoginPage()
        self.loginpage.login('admin', 'admin')
        self.cp = CustomerPage()
        self.sp = SearchPage()
        self.db = DbCustomer()
        self.db.delete_customer('c004')


    def test_1_customer_add_suc(self):
        #添加客户
        self.cp.customer_add(customer_no='c004',customer_name='mike')
        #获取实际值
        actual_text = self.cp.customer_add_suc_text()
        self.sp.search('c004')
        cus_data_page = self.sp.get_data_one()
        cus_data_db = self.db.add_cus_data_one('c004')
        print(cus_data_page,cus_data_db)
        self.assertEqual(actual_text,'添加记录成功！')
        self.assertEqual(cus_data_page,cus_data_db)



    def tearDown(self) -> None:
        UseBrowser.quit()


    # def test_2_customer_add_suc(self):
    #     self.cp.customer_add('c009','mike')
    #     actual_text = self.cp.customer_add_suc_text()
    #     # print(actual_text)
    #     self.assertEqual(actual_text, '添加记录成功！')
        # self.cp.compare_contain()
        # self.assertTrue()

    # def test_3_customer_add_suc(self):
    #     self.cp.customer_add('c009','mike')
    #     actual_text = self.cp.customer_add_suc_text()
    #     # print(actual_text)
    #     self.assertEqual(actual_text, '添加记录成功！')



    # def test_2_customer_add_suc(self):
    #     self.cp.customer_add('c004')


if __name__ == '__main__':
    unittest.main()
