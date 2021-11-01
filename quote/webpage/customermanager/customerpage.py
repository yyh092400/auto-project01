
from quote.base.operationbrowser import OperationBrowser
from quote.base.usebrowser import UseBrowser
from quote.util.loginfo import AutoLog


class CustomerPage:


    def __init__(self):
        self.ob = OperationBrowser(UseBrowser.driver)

    def customer_add(self,customer_no='',customer_name='',customer_tel='',customer_address='',customer_relationman='',
                     customer_other_info=''):

        self.ob.change_frame('Links')
        self.ob.click('xpath','//*[@id="Bar_panel0_b0"]/img')
        self.ob.change_frame('main')
        self.ob.click('xpath','/html/body/center/table[2]/tbody/tr[2]/td[2]/a')
        self.ob.change_window('新增客户信息')
        self.ob.input_text('name','customerNO',customer_no)
        self.ob.input_text('name', 'customerName',customer_name)
        self.ob.input_text('name', 'phone',customer_tel)
        self.ob.input_text('name','address',customer_address)
        self.ob.input_text('name','relationman',customer_relationman)
        self.ob.input_text('name', 'otherInfo', customer_other_info)
        self.ob.click('name','saveButton')



    def customer_add_suc_text(self):
        return self.ob.get_text_xpath('/html/body/center')[0:7]
        # pass

    def seache_resutl(self):
        pass

    #
    # def compare_contain(self,name,lst):
    #     if name in lst:
    #         return True
    #     else:
    #         return False

