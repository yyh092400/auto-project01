

from quote.util.loginfo import AutoLog


class OperationBrowser:

    def __init__(self,driver):
        self.driver = driver
        self.logger = AutoLog()

    #打开浏览器
    def open_url(self,url):
        self.driver.get(url)

    #通过name输入文本
    def input_text(self,type,locator,text):
        self.logger.set_info('info','输入内容:'+text)
        if type.lower() == 'name':
            self.driver.find_element_by_name(locator).send_keys(text)
        elif type.lower() == 'id':
            self.driver.find_element_by_id(locator).send_keys(text)
        elif type.lower() == 'xpath':
            self.driver.find_element_by_xpath(locator).send_keys(text)

    #点击
    def click(self,type,locator):
        self.logger.set_info('info', '点击按钮:' + locator)
        if type.lower() == 'name':
            self.driver.find_element_by_name(locator).click()
        elif type.lower() == 'xpath':
            self.driver.find_element_by_xpath(locator).click()
    #切换frame
    def change_frame(self,name):
        self.logger.set_info('info', '切换frame:' + name)
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(name)

    #获取页面文本
    def get_text_xpath(self, locator):
        content=self.driver.find_element_by_xpath(locator).text
        self.logger.set_info('info','获取页面文本内容:'+content)
        return content


    #切换窗体
    def change_window(self,title):
        self.logger.set_info('info', '切换窗体:' +title)
        for window_id in self.driver.window_handles:
            self.driver.switch_to.window(window_id)
            if self.driver.title == title:
                break


    def get_element_xpath(self,locator):
        return self.driver.find_element_by_xpath(locator)


    def get_tags_name(self,scope,element):
        return scope.find_elements_by_tag_name(element)

    # def get_element(self):







    # #切换frame
    # def change_frame(self,name):
    #     self.driver.switch_to.default_content()
    #     self.driver.switch_to.frame(name)
    #
    # #获取文本信息
    # def get_text_xpath(self,locator):
    #     return  self.driver.find_element_by_xpath(locator).text




# if __name__=='__main__':
#     ub = UseBrowser('chrome','../chromedriver.exe')
#     ob = OperationBrowser(UseBrowser.driver)
#     ob.open_url('http://localhost:8080/JavaPrj_6/')
#     time.sleep(3)
#     ob.input_text_name('username','admin')
#     time.sleep(3)
#     ob.input_text_name('password', 'admin')
#     time.sleep(3)
#     ob.click_name('submit')