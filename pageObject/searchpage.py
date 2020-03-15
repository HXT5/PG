from basePage.base import Base
from selenium import webdriver
from selenium.webdriver.common.by import By
class SearchPage(Base):
    #输入
    def send_words(self,locator,text):
       self.send_keys_element(locator,text)
    #点击
    def click_button(self,locator):
        self.click_element(locator)

if __name__ == '__main__':

    a=SearchPage("chrome")
    a.get_url("http://www.baidu.com")
    a.send_words((By.ID,"kw"),"测试")
    a.click_button((By.ID,"su"))