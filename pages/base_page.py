import time
import os
import logging

from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from configs.constants import IMG_DIR


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.driver.maximize_window()

    def wait_click_element(self, locator, timeout=20) -> WebElement:
        """等待元素可点击"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(EC.element_to_be_clickable(locator))
        except (TimeoutException, NoSuchElementException) as e:
            logging.error('元素没有定位到')
            self.screen_shot()
            raise e

    def wait_presence_element(self, locator, timeout=20) -> WebElement:
        """等待元素出现"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(EC.presence_of_element_located(locator))
        except (TimeoutException, NoSuchElementException) as e:
            logging.error('元素没有定位到')
            self.screen_shot()
            raise e

    def wait_visibility_element(self, locator, timeout=20) -> WebElement:
        """等待元素可见"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(EC.visibility_of_element_located(locator))
        except (TimeoutException, NoSuchElementException) as e:
            logging.error('元素没有定位到')
            self.screen_shot()
            raise e

    def screen_shot(self):
        """截图，保存到指定的位置"""
        current_time_str = time.strftime('%Y%m%d%H%M%S', time.localtime())
        return self.driver.save_screenshot(os.path.join(IMG_DIR, current_time_str + '.png'))

    def ele_click(self, locator):
        """点击元素"""
        return self.wait_click_element(locator).click()

    def alert_handler(self, timeout=20, action='accept'):
        """等待alert出现"""
        WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        message = alert.text
        if action == 'accept':
            alert.accept()
        else:
            alert.dismiss()
        return message
