import pytest
import allure
class Test01:
    def setup(self):
        pass
    def teardown(self):
        pass
    @allure.step(title="测试步骤1")
    def test01(self):
        print("1")

    @allure.step(title="测试步骤21")
    def test02(self):
        print("2")