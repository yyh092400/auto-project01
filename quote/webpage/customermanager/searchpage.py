
import time

from quote.base.operationbrowser import OperationBrowser
from quote.base.operationextendone import OperationBrowserEx
from quote.base.usebrowser import UseBrowser


class SearchPage:


    def __init__(self):
        self.ob = OperationBrowser(UseBrowser.driver)
        self.oc = OperationBrowserEx(UseBrowser.driver)


    def search(self,customer_no='',customer_name='',customer_tel='',customer_address='',
               customer_relationman='',customer_other_info=''):
        self.ob.change_window('报价管理系统')
        self.ob.change_frame('Links')
        self.ob.click('xpath', '//*[@id="Bar_panel0_b1"]/img')
        self.ob.change_frame('main')
        self.ob.input_text('name', 'customerNO', customer_no)
        self.ob.input_text('name', 'customerName', customer_name)
        self.ob.input_text('name', 'phone', customer_tel)
        self.ob.input_text('name', 'address', customer_address)
        self.ob.input_text('name', 'relationman', customer_relationman)
        self.ob.input_text('name', 'otherInfo', customer_other_info)
        self.ob.click('xpath', '/html/body/center/form/table[3]/tbody/tr/td/input')


    def get_data_first_page(self):
        # lst_s=[]
        # for i in range(1,5):
        #     lst=[]
            # for row in range(2,7):
            #     for col in range(1,7):
            #         v = self.ob.get_text_xpath('/html/body/center/form/table[1]/tbody/tr[{}]/td[{}]'.format(row,col))
            #         if v == '':
            #             pass
            #         else:
            #             lst.append(v)
        lst = []
        table=self.ob.get_element_xpath('/html/body/center/form/table[1]/tbody')
        tr_lst = self.ob.get_tags_name(table,'tr')
        for tr_element in tr_lst[1:]:
            for td_element in self.ob.get_tags_name(tr_element,'td')[:-1]:
                if self.oc.get_element_text(td_element)=='':
                    pass
                else:
                    lst.append(self.oc.get_element_text(td_element))
        return lst



    def get_data_one(self):

        '/html/body/center/form/table[1]/tbody/tr[2]/td[1]'
        lst= []
        for td in range(1,7):
            td_text = self.ob.get_text_xpath('/html/body/center/form/table[1]/tbody/tr[2]/td[{}]'.format(td))
            if td_text != '':
                lst.append(td_text)
        lst.sort()
        return lst


            # lst_s.append(lst)
            # self.ob.click('xpath','/html/body/center/form/table[2]/tbody/tr/td/a[{}]'.format(i))
            # time.sleep(1)
            # print(lst)
