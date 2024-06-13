import unittest
from selenium.webdriver import Chrome

import ddt

from pages.login_page import LoginPage
from pages.home_page import HomePage
from datas.login_data import login_invalid, login_error, login_success


@ddt.ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = Chrome()
        self.driver.implicitly_wait(20)
        self.login_page = LoginPage(self.driver)
        self.home_page = HomePage(self.driver)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def setUp(self):
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.refresh()

    @ddt.data(*login_error)
    def test_1_login_error(self, user_info):
        # 在一个函数里面运行多个数据：for
        # 如果我想测试 3 个登录错误异常用例。
        # self.assert()   # if expect == actual: print(True)
        self.login_page.login(user_info[0], user_info[1])
        actual_ele = self.login_page.get_element_error_info()
        # if 是不不是在首页，driver.current_url：定位某一个元素，: 20

        self.assertEqual(actual_ele.text, user_info[2])
        #

    @ddt.data(*login_invalid)
    def test_2_login_invalid(self, user_info):
        self.login_page.login(user_info[0], user_info[1])
        actual_ele = self.login_page.get_element_invalid_info()
        self.assertEqual(actual_ele.text, user_info[2])

    @ddt.data(*login_success)
    def test_3_success(self, user_info):
        # 应该包含哪一些代码？
        self.login_page.login(user_info[0], user_info[1])
        user = self.home_page.get_element_user()
        self.assertEqual(user_info[2], user.text)


if __name__ == '__main__':
    unittest.main()
