import pytestimport allurefrom pageObject.searchpage import SearchPagefrom selenium import webdriverfrom selenium.webdriver.common.by import Byclass Test01:    def setup_class(self):        self.driver=SearchPage("chrome")        self.driver.get_url("http://www.baidu.com")    def teardown_class(self):        #self.driver.quit_browser()        pass    @allure.step(title="测试步骤1")    def test01(self):        self.driver.send_words((By.ID, "kw"), "测试")        self.driver.click_button((By.ID, "su"))    @allure.step(title="测试步骤2")    def test02(self):        print("2")