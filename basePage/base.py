from selenium import webdriver

class Base(object):
    #初始化
    def __init__(self,browser):
        if browser.lower() =="chrome":
              self.driver=webdriver.Chrome()
        else:
              self.driver=webdriver.ie()
    #访问URL
    def get_url(self,url):
        return self.driver.get(url)
    #元素定位
    def  find_element(self,locator):
        return self.driver.find_element(*locator)

    def click_element(self,locator):
        self.find_element(locator).click()

    def send_keys_element(self,locator,text):
        self.find_element(locator).send_keys(text)
    #关闭浏览器
    def quit_browser(self):
        self.driver.quit()

