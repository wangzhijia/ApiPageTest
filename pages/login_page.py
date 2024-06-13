
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def wait_click_element(self, locator):
        wait = WebDriverWait(self.driver, 20)
        return wait.until(EC.element_to_be_clickable(locator))

    def wait_presence_element(self, locator):
        wait = WebDriverWait(self.driver, 20)
        return wait.until(EC.presence_of_element_located(locator))

    def login(self, username, pwd):
        # 1、输入网址，get
        self.driver.get('http://120.78.128.25:8765/Index/login.html')
        username_ele = self.get_element_username()
        pwd_ele = self.get_element_pwd()
        # 输入用户名和密码
        username_ele.send_keys(username)
        pwd_ele.send_keys(pwd)
        # 提交
        submit = self.driver.find_element_by_xpath("//button[contains(@class, 'btn-special')]").click()

    def click_login(self):
        return self.driver.find_element_by_css_selector("a[href='/Index/login.html']").click()

    def get_element_error_info(self):
        """用户信息格式不正确"""
        return self.wait_presence_element((By.CLASS_NAME, "form-error-info"))

    def get_element_invalid_info(self):
        """用户密码不对"""
        return self.wait_presence_element((By.CLASS_NAME, "layui-layer-content"))

    def get_element_username(self):
        """定位用户名"""
        return self.wait_presence_element((By.NAME, 'phone'))

    def get_element_pwd(self):
        """定位密码"""
        return self.wait_presence_element((By.NAME, 'password'))

