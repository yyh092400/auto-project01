
from selenium import webdriver
# import time
class UseBrowser:

    driver = None


    def __init__(self,browser_name,path):

        if browser_name == 'chrome':
            self.driver = webdriver.Chrome(path)
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)
            UseBrowser.driver = self.driver

        elif browser_name == 'firefox':
            self.driver = webdriver.Firefox(path)
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)
            UseBrowser.driver = self.driver
            self.driver.find_element_by_xpath().send_keys()



    @classmethod
    def quit(self):
        UseBrowser.driver.quit()

# if __name__=='__main__':
#     browser = UseBrowser('chrome','../chromedriver.exe')
#     time.sleep(3)
#     UseBrowser.quit()