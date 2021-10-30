# -*- coding: utf-8 -*-
# @Time : 2021-10-27 11:14
# @Author : bai ping
# @QQ : 376706275



class OperationBrowserEx:

    def __init__(self,driver):
        self.driver = driver


    def get_element_text(self,element):
        return element.text